from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    comentario = models.CharField(max_length=300)

class Restaurante(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField()
    comentario = models.CharField(max_length=300)
    calificacion = models.IntegerField()
    tipoDeComida = models.CharField(max_length=30)
    categoriaPrecio = models.CharField(max_length=30)
