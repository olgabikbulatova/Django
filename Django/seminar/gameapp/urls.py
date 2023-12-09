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
from .views import index, head_tails, cubes, hundred, about, headtails_values, rolls, game_roll


urlpatterns = [
    path('', index, name='index'),
    path('headtails', head_tails, name='head_tails'),
    path('headtails_values', headtails_values, name='headtails_values'),
    path('cubes', cubes, name='cubes'),
    path('hundred/', hundred, name='hundred'),
    path('about/', about, name='about'),
    path('rolls/<int:roll>', rolls, name='rolls'),
    path('headtails/<int:roll>', game_roll, name='ht_roll'),
    path('cubes/<int:roll>', game_roll, name='ht_roll'),
    path('hundred/<int:roll>', game_roll, name='ht_roll'),
]