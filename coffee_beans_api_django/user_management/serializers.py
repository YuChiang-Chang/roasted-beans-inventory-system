from rest_framework import serializers
# from django.contrib.auth.models import Permission
from .models import CustomUser, Role, CustomPermission

class CustomPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPermission
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    permissions = CustomPermissionSerializer(many=True)

    class Meta:
        model = Role
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    roles = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all() ,many=True, required=False)
    permissions = serializers.PrimaryKeyRelatedField(queryset=CustomPermission.objects.all() ,many=True, required=False)

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def create(self, validated_data):
        roles_data = validated_data.pop('roles', [])
        permissions_data = validated_data.pop('permissions', [])
        password = validated_data.pop('password')

        user = CustomUser.objects.create_user(
            **validated_data,
            password=password,
        )
        user.roles.set(roles_data)
        user.permissions.set(permissions_data)
        return user
    
    def update(self, instance, validated_data):

        # 檢查是否是超級用戶且請求由非超級用戶發起
        if instance.is_superuser and not self.context['request'].user.is_superuser:
            # 如果目標是超級用戶且請求者不是超級用戶，則不允許修改電子郵件、密碼、角色和權限
            raise serializers.ValidationError("您無權修改超級用戶的資料。")
        
        # 如果不是針對超級用戶或請求者也是超級用戶，則正常處理角色和權限的更新
        roles_data = validated_data.pop('roles', None)
        if roles_data is not None:
            instance.roles.set(roles_data)

        permissions_data = validated_data.pop('permissions', None) 
        if permissions_data is not None:
            instance.permissions.set(permissions_data)

        # 更新密碼，如果有提供的話
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        # 更新其他欄位
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('password',None)
        return representation