from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, UserViewSet, PermissionViewSet, RoleViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = [
    # path('create_user/', CreatUserView.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
