from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name = 'index'),
     path('mostrarPersonas', views.mostrarPersonas, name = 'MostrarP'),
     path('mostrarAutos', views.mostrarAutos, name = 'MostrarA'),
     path('registroA', views.registroA, name = 'RegistroA'),
]  


