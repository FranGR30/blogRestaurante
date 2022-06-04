from django.urls import URLPattern, path
from.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login',iniciarSesion, name='login'),
    path('register',register, name='register'),
    path('logout',LogoutView.as_view(template_name='AppBlog/index.html'), name='logout'),
    path('editarPerfil',editarPerfil, name='editarPerfil'),
]