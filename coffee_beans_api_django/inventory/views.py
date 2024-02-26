from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import CoffeeBean
from .serializers import CoffeeBeanSerializer

class CoffeeBeanViewSet(viewsets.ModelViewSet):
    # 指定要操作的數據集
    queryset = CoffeeBean.objects.all()
    # 指定用於序列化/反序列化的類
    serializer_class = CoffeeBeanSerializer

