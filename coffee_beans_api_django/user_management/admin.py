from django.contrib import admin

# Register your models here.
from .models import CustomPermission, CustomUser, Role

admin.site.register(CustomPermission)
admin.site.register(CustomUser)
admin.site.register(Role)