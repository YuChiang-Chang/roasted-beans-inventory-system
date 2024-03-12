from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, UserViewSet, PermissionViewSet, RoleViewSet, UserProfileView
from .views import TestTokenView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = [
    # path('create_user/', CreatUserView.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    # path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('', include(router.urls)),
    path('test-token/', TestTokenView.as_view(), name='test-token'),
]
