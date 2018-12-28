"""Definiuje wzorce adresów URL dla learning_logs"""

from django.urls import path

from . import views

urlpatterns = [
    #Strona główna
    path(r'', views.index, name='index'),
]
