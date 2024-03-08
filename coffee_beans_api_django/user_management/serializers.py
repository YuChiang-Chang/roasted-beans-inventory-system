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
    # isAdmin = serializers.BooleanField(source='is_superuser', read_only=True)
    roles = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all() ,many=True, required=False)
    permissions = serializers.PrimaryKeyRelatedField(queryset=CustomPermission.objects.all() ,many=True, required=False)

    class Meta:
        model = CustomUser
        # fields = ['id', 'email', 'password']
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    # def get_isAdmin(self, obj):
    #     return obj.is_superuser

    def create(self, validated_data):
        roles_data = validated_data.pop('roles', [])
        permissions_data = validated_data.pop('permissions', [])
        password = validated_data.pop('password')

        user = CustomUser.objects.create_user(
            **validated_data,
            # email=validated_data['email'],
            password=password,
            # is_staff=validated_data.get('is_staff', False),
        )
        user.roles.set(roles_data)
        user.permissions.set(permissions_data)
        return user
    
    def update(self, instance, validated_data):
        # roles_data = validated_data.pop('roles', [])
        # permissions_data = validated_data.pop('permissions', [])

        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        


        # instance.roles.set(roles_data)
        # instance.permissions.set(permissions_data)
        if 'roles' in validated_data:
            roles_data = validated_data('roles')
            instance.roles.set(roles_data)
        if 'permissions' in validated_data:
            permissions_data = validated_data.pop('permissions', [])
            instance.permissions.set(permissions_data)
            
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # instance.email = validated_data.get('email', instance.email)
        # if 'password' in validated_data:
        #     instance.set_password(validated_data['password'])
        #     instance.is_active = validated_data.get('is_active', instance.is_active)
        #     instance.save()
        return instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('password',None)
        return representation