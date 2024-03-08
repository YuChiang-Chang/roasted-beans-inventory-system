from django.contrib import admin
# from django import forms
# from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import CustomPermission, CustomUser, Role


# class CustomUserForm(forms.ModelForm):
#     permissions = forms.ModelMultipleChoiceField(
#         queryset=Permission.objects.all(),
#         required=False,
#         widget=forms.CheckboxSelectMultiple
#     )

#     class Meta:
#         model = CustomUser
#         fields = '__all__'

# class CustomUserAdmin(UserAdmin):
#     form = CustomUserForm
#     model = CustomUser
#     fieldsets = (
#         (None, {'fields': ('email', 'password', 'permissions', 'roles', 'is_staff', 'is_active', 'is_superuser')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )
#     # 定制列表顯示
#     list_display = ['email', 'is_staff', 'is_active', 'is_superuser']
#     list_filter = ['is_staff', 'is_active', 'is_superuser']
#     search_fields = ['email']
#     ordering = ['email']

#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         if 'permissions' in form.cleaned_data:
#             obj.permissions.set(form.cleaned_data['permissions'])

admin.site.register(CustomPermission)
admin.site.register(CustomUser)
# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role)