from django.shortcuts import render
from .models import autos
# Create your views here.

def index(request):
	return render(request, 'vistas/login.html', {})

def mostrarPersonas(request):
	return render(request, 'vistas/re_personas.html', {})

def mostrarAutos(request):
	return render(request, 'vistas/re_autos.html', {})	

def registroA(request):
    qs_autos = autos.objects.all()
    return render(request, 'vistas/registro.html', {'v_autos':qs_autos})


