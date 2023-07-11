from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registeruser, name='register'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('profile/<int:pk>/', views.userprofile, name='profile'),
    path('', views.home, name="home"),

    # API
    path('api/users/', views.getusers, name='getusers_api'),
]