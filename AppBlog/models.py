
from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%d%m%Y%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('restaurante/', filename)

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    def __str__(self):
        return self.nombre+" "+self.apellido

class Restaurante(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField()
    comentario = models.CharField(max_length=300)
    calificacion = models.IntegerField()
    tipoDeComida = models.CharField(max_length=30)
    categoriaPrecio = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to=filepath, null=True,blank=True)
    autor = models.TextField(max_length=50)
    fecha = models.DateField()

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', null=True,blank=True)
