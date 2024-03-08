from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class CustomPermission(models.Model):
    codename = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="custom_permissions")
    description = models.TextField(blank=True)

    def __str__(self):
        # 返回`auth.add_user (Can add user)`
        # return f"{self.content_type.app_label}.{self.codename} ({self.name})"
        return self.name
    
class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    permissions = models.ManyToManyField(CustomPermission, related_name='roles')

    def __str__(self):
        return self.name


# class SimplePermission(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    
# class User(models.Model):
# class CustomUserModel(models.Model):
#     email = models.EmailField(unique=True)
#     permissions = models.ManyToManyField(CustomPermission, blank=True, related_name='users')

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('用戶必須有一個電子郵件地址')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser 必須設定 is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser 必須設定 is_superuser=True.')

        return self.create_user(email, password, **extra_fields)       
    

class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='電子郵件地址', max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    roles = models.ManyToManyField(Role, blank=True)
    permissions = models.ManyToManyField(CustomPermission, related_name='users', blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def get_custom_permissions(self):
        # 直接獲取的權限
        direct_permissions = self.permissions.all()
        # 通過角色獲得的權限
        role_permissions = CustomPermission.objects.filter(roles__in=self.roles.all()).distinct()
        # 合併這兩種權限，使用 set 來去除可能的重複項
        all_permissions = set(list(direct_permissions) + list(role_permissions))
        return all_permissions

    def has_perm(self, perm, obj=None):
        "用戶是否有特定權限？"
        if self.is_superuser:
            return True
        # 檢查用戶是擁有指定的權限
        # return self.permissions.filter(codename=perm).exists() or \
        #     any(Role.permissions.filter(codename=perm).exists() for role in self.roles.all())
    
    def has_module_perms(self, app_label):
        "用戶是否有權查看 app_label 應用的權限？"
        if self.is_superuser:
            return True
        # 檢查用戶是否有權查看指定app_label下的任何權限
        # return self.permissions.filter(content_type__app_label=app_label).exists() or \
        #     any(Role.permissions.filter(content_type__app_label=app_label).exists() for role in self.roles.all())