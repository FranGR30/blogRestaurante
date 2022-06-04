from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponse
from .forms import *
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'AppBlog/index.html')

def register(request):
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            formulario.save()
            return render(request,'AppBlog/index.html',{'mensaje':f'Usuario:{username} creado exitosamente'})
        else:
            return render(request,'AppBlog/index.html',{'mensaje':'no se pudo crear el usuario'})
    else:
        formulario = UserRegistrationForm()
        return render(request,'AppBlog/register.html',{'formulario':formulario})

def iniciarSesion(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            clave = formulario.cleaned_data.get('password')
            user = authenticate(username = usuario, password = clave)
            if user is not None:
                login(request,user)
                return render(request,'AppBlog/index.html',{'usuario':usuario,'mensaje':'Bienvenido al sistema'})
            else:
                return render(request,'AppBlog/login.html',{'formulario':formulario,'mensaje':'Usuario incorrecto, vuelva a loguearse'})
        else:
            return render(request,'AppBlog/login.html',{'formulario':formulario,'mensaje':'formulario invalido, vuelva a loguearse'})
    else:
        formulario = AuthenticationForm()
        return render(request,'AppBlog/login.html',{'formulario':formulario})

@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method == 'POST':
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            return render(request, 'AppBlog/index.html', {'usuario':usuario, 'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request, 'AppBlog/editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username})