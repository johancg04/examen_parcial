from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login(request):
    return render(request, 'login.HTML')


def gestionUsuarios(request):
    return render(request, 'gestion_usuarios.HTML')


def gestionProductos(request):
    return render(request, 'gestion_productos.HTML')


def cerrarSesion(request):
    return render(request, 'login.HTML')
