from django.urls import URLPattern, path
from.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls import static

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login',iniciarSesion, name='login'),
    path('register',register, name='register'),
    path('logout',LogoutView.as_view(template_name='AppBlog/index.html'), name='logout'),
    path('editarPerfil',editarPerfil, name='editarPerfil'),
    path('agregarAvatar',agregarAvatar, name='agregarAvatar'),
    path('buscarRestaurante',buscarRestaurante, name='buscarRestaurante'),
    path('mostrarRestaurante/<str:pk>',mostrarRestaurante, name='mostrarRestaurante'),
    path('eliminarPost/<str:pk>',eliminarPost, name='eliminarPost'),
    path('editarPost/<str:pk>',editarPost, name='editarPost'),
    path('crearPost',crearPost, name='crearPost'),
]

