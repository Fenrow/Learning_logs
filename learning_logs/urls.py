"""Definiuje wzorce adresów URL dla learning_logs"""

from django.urls import path, re_path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #Strona główna
    path(r'', views.index, name='index'),
    #Wyświetlanie listy tematów
    path(r'topics/', views.topics, name='topics'),
    #Strona szczegółowa dotycząca pojedyńczego tematu
    re_path(r'topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
    #Strona odpowiedzialna za utworzenie nowego tematu
    path(r'new_topic/', views.new_topic, name='new_topic'),
    #Strona odpowiedzialna za dodanie wpisu do konkretnego tematu
    re_path(r'new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),
]
