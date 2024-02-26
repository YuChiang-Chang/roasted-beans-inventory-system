"""
URL configuration for coffee_beans_api_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.views import CoffeeBeanViewSet

# 通過register方法將CoffeeBeanViewSet與一個路由前綴'coffeebeans'關聯起來。
# 這意味著所有關於CoffeeBean的API端點都將以/coffeebeans/作為URL前綴。
router = DefaultRouter()
router.register(r'coffeebeans', CoffeeBeanViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
