from django.db import models
from django.contrib.auth.models import User

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

class Avatar(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatar',blank = True,null = True)
