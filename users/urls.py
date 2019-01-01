"""Definicja wzorców adresów URL dla aplikacji users"""

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
    #Strona logowania
    path(r'login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    #Strona Wylogowania
    path(r'logout/', auth_views.LogoutView.as_view(), name='logout'),
    #Strona rejestracji
    path(r'register/', views.register, name='register'),
]
