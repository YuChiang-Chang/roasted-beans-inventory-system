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

# class CreatUserView(APIView):
#     def post(self, request, format=None):
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({"message": "用戶創建成功", "userId": user.id}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
            # login(request, user)
            return Response({
                'email': user.email,
                'token': token.key,
                'isAdmin': user.is_superuser,
                'permissions': permissions_data,
                }, status=status.HTTP_200_OK)
        else:
            return Response({"message": "無效的憑證"}, status=status.HTTP_401_UNAUTHORIZED)
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsAuthenticated]

    # @action(detail=True, methods=['post'], url_path='update-permissions')
    # def update_permissions(self, request, pk=None):
    #     user = self.get_object()
    #     permissions_data = request.data.get('permissions', [])
    #     roles_data = request.data.get('roles', [])

    #     # 更新用戶權限
    #     permissions = CustomPermission.objects.filter(id__in=permissions_data)
    #     user.permissions.set(permissions)

    #     # 更新用戶角色
    #     roles = Role.objects.filter(id__in=roles_data)
    #     user.roles.set(roles)
    
    #     return Response({'status': 'permissions updated'})
        

class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomPermission.objects.all()
    serializer_class = CustomPermissionSerializer

class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

