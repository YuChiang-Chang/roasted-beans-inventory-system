from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .models import CustomUser, CustomPermission, Role
from .serializers import CustomUserSerializer, CustomPermissionSerializer, RoleSerializer

class LoginView(APIView):
    def post(self, request, format=None):
        # 從請求中獲取資料
        email = request.data.get('email')
        password = request.data.get('password')

        # 使用 Django 的 authenticate 方法來驗證資料
        user = authenticate(username=email, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            permissions = user.get_custom_permissions()

            permissions_data = [permission.codename for permission in permissions]
            return Response({
                'email': user.email,
                'token': token.key,
                'isAdmin': user.is_superuser,
                'permissions': permissions_data,
                }, status=status.HTTP_200_OK)
        else:
            return Response({"message": "無效的憑證"}, status=status.HTTP_401_UNAUTHORIZED)

class UserProfileView(APIView):
    # 確認已認證的用戶可以訪問這個視圖
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomPermission.objects.all()
    serializer_class = CustomPermissionSerializer

class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class TestTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, world! Your token is valid!'}
        return Response(content)

