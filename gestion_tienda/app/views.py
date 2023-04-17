from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.


def loginUser(request):
    if request.method == 'POST':
        nombreUsuario = request.POST.get('nombreUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        usuarioInfo = authenticate(
            request, username=nombreUsuario, password=contraUsuario)
        if usuarioInfo is not None:
            login(request, usuarioInfo)
            if usuarioInfo.datosusuario.rolUsuario == 'ADMINISTRADOR':
                return render(request, 'gestion_usuarios.html', {
                    'usuariosTotales': User.objects.all().order_by('id')
                })
            else:
                return HttpResponseRedirect(reverse('app:gestionProductos', kwargs={'ind': usuarioInfo.id}))
        else:
            return HttpResponseRedirect(reverse('app:login'))
    return render(request, 'login.html')


def gestionUsuarios(request):
    return render(request, 'gestion_usuarios.HTML')


def gestionProductos(request):
    return render(request, 'gestion_productos.HTML')


def cerrarSesion(request):
    return render(request, 'login.HTML')
