from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('login', views.loginUser, name = 'login'),
    path('', views.index, name = 'index'),
    path('base',views.base, name = 'base'),
    path('home', views.homeUser, name = 'home'),
    path('logout', views.logoutUser, name = 'logout'),
    path('add', views.add, name = 'add')
   
]
