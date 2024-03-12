from django.apps import AppConfig


class UserManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_management'

    def ready(self):
        # . 表示當前包
        from . import signals
