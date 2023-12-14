"""
URL configuration for seminar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import index, client, product, order, del_client, find_client, add_client, update_client, new_order, \
    client_order, client_product, update_product

urlpatterns = [
    path('', index, name='index'),
    path('client', client, name='client'),
    path('product', product, name='product'),
    path('order', order, name='order'),
    path('del_client/<int:id>/', del_client, name='del_client'),
    path('client/<int:id>/', find_client, name='find_client'),
    path('add_client', add_client, name='add_client'),
    path('client_upd/<int:id>/', update_client, name='upd_client'),
    path('new_order', new_order, name='new_order'),
    path('client_order/<int:client_id>', client_order, name='cl_order'),
    path('client_product/<int:client_id>', client_product, name='cl_prod'),
    path('product/edit/<int:id>', update_product, name='update_product'),
]
