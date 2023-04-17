from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class datosUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rolUsuario = models.CharField(max_length=32, default='USUARIO')
    nroCelular = models.CharField(max_length=32, default='987654321')
    fechaIngreso = models.DateField(default=date.today)
    nombre = models.CharField(max_length=32, default='Nombre')
    apellido = models.CharField(max_length=32, default='Apellido')
    email = models.CharField(max_length=32, default='email')
