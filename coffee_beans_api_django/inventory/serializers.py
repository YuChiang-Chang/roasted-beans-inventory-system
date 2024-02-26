from rest_framework import serializers
from .models import CoffeeBean

class CoffeeBeanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeBean
        # 指定要序列化的字段，'__all__'表示所有字段
        fields = '__all__'
    
    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("重量不能為負數。")
        return value
