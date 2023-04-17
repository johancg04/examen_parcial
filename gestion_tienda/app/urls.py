from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('login', views.loginUser, name='login'),
    path('gestionUsuarios', views.gestionUsuarios, name='gestionUsuarios'),
    path('gestionProductos', views.gestionProductos, name='gestionProductos'),
    path('cerrarSesion', views.cerrarSesion, name='cerrarSesion'),
]
