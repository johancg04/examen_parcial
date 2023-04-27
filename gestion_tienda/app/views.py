from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import datosUsuario

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
    if request.user.datosusuario.rolUsuario == 'ADMINISTRADOR':
        if request.method == 'POST':
            nombreUsuario = request.POST.get('nombreUsuario')
            apellidoUsuario = request.POST.get('apellidoUsuario')
            emailUsuario = request.POST.get('emailUsuario')
            contrasenaUsuario = request.POST.get('passwordUsuario')
            fechaIngreso = request.POST.get('fechaUsuario')
            nroCelular = request.POST.get('celUsuario')
            usernameUsuario = request.POST.get('usernameUsuario')
            rolUsuario = request.POST.get('rolUsuario')

            usuarioNuevo = User.objects.create(
                username=usernameUsuario,
                email=emailUsuario
            )
            usuarioNuevo.set_password(contrasenaUsuario)
            usuarioNuevo.first_name = nombreUsuario
            usuarioNuevo.last_name = apellidoUsuario
            usuarioNuevo.is_staff = True
            usuarioNuevo.save()

            datosUsuario.objects.create(
                user=usuarioNuevo,
                rolUsuario=rolUsuario,
                nroCelular=nroCelular,
                fechaIngreso=fechaIngreso
            )
            return HttpResponseRedirect(reverse('app:gestionUsuarios'))
        else:
            return render(request, 'gestion_usuarios.HTML')
    else:
        return render(request, 'gestion_usuarios.HTML')


def gestionProductos(request):
    return render(request, 'gestion_productos.HTML')


def cerrarSesion(request):
    return render(request, 'login.HTML')


def eliminarUsuario(request, ind):
    usuarioEliminar = User.objects.get(id=ind)
    datosUsuario.objects.get(user=usuarioEliminar).delete()
    usuarioEliminar.delete()
    return HttpResponseRedirect(reverse('app:gestionUsuarios'))
