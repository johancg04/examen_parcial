from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('gestionUsuarios', views.gestionUsuarios, name='gestionUsuarios'),
    path('gestionProductos', views.gestionProductos, name='gestionProductos'),
    path('cerrarSesion', views.cerrarSesion, name='cerrarSesion'),
]
