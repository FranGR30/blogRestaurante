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
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user)
        if avatar:
            return render(request, 'AppBlog/index.html', {'url':avatar[0].avatar.url})

    return render(request, 'AppBlog/index.html')

def register(request):
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            formulario.save()
            if(formulario.save):
                user=User.objects.get(username=username)
                avatar = Avatar(user=user,avatar='avatar/generico.jpg')
                avatar.save()
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
                avatar = Avatar.objects.filter(user=request.user)
                return render(request,'AppBlog/index.html',{'usuario':usuario,'mensaje':'Bienvenido al sistema','url':avatar[0].avatar.url})
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
    avatar = Avatar.objects.filter(user=request.user)
    if request.method == 'POST':
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            return render(request, 'AppBlog/index.html', {'usuario':usuario, 'mensaje':'PERFIL EDITADO EXITOSAMENTE','url':avatar[0].avatar.url})
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request, 'AppBlog/editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username,'url':avatar[0].avatar.url})

@login_required
def agregarAvatar(request):

    user=User.objects.get(username=request.user)
    avatar = Avatar.objects.filter(user=request.user)

    if request.method == "POST":
         formulario = AvatarForm(request.POST, request.FILES)
         if formulario.is_valid():

             avatarViejo = Avatar.objects.get(user=request.user)
             if(avatarViejo.avatar):
                avatarViejo.delete()
             avatar = Avatar(user=user,avatar= formulario.cleaned_data['avatar'])
             avatar.save()
             avatar = Avatar.objects.filter(user=request.user)
             return render(request, 'AppBlog/index.html', {'usuario': user , 'mensaje': 'Avatar cambiado exitosamente','url':avatar[0].avatar.url})
    else:
        formulario=AvatarForm()
    return render(request, 'AppBlog/agregarAvatar.html', {'formulario': formulario, 'usuario': user,'url':avatar[0].avatar.url})

def buscarRestaurante(request):
    restaurantes = Restaurante.objects.all()
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user)
        if avatar:
            return render(request, 'AppBlog/buscarRestaurante.html', {'url':avatar[0].avatar.url,'restaurantes':restaurantes})
    return render(request, 'AppBlog/buscarRestaurante.html',{'restaurantes':restaurantes})
    
@login_required
def mostrarRestaurante(request,pk):
    user=request.user
    avatar = Avatar.objects.filter(user=request.user)
    restauranteIndividual = Restaurante.objects.get(id=pk)
    return render(request, 'AppBlog/mostrarRestaurante.html',{'restauranteIndividual':restauranteIndividual,'url':avatar[0].avatar.url})

@login_required
def eliminarPost(request,pk):
    avatar = Avatar.objects.filter(user=request.user)
    restauranteIndividual = Restaurante.objects.get(id=pk)
    user = request.user
    if user.groups.filter(name='admin').exists():
        restauranteIndividual.delete()
        return render(request, 'AppBlog/index.html',{'mensaje':"El post se elimino correctamente",'url':avatar[0].avatar.url})
    else:
        return render(request, 'AppBlog/index.html',{'mensaje':"Solo el administrador puede realizar esta accion",'url':avatar[0].avatar.url})

@login_required
def editarPost(request, pk):
    avatar = Avatar.objects.filter(user=request.user)
    restaurante = Restaurante.objects.get(id=pk)
    user = request.user
    if user.groups.filter(name='admin').exists():
        if request.method == "POST":
            formulario = EditPost(request.POST.get)
            restaurante.direccion = request.POST.get('direccion')
            restaurante.telefono = request.POST.get('telefono')
            restaurante.calificacion = request.POST.get('calificacion')
            restaurante.comentario = request.POST.get('comentario')
            restaurante.save()
            return render(request, 'AppBlog/index.html',{'mensaje':"El post se edito correctamente",'url':avatar[0].avatar.url})
        else:
            formulario = EditPost()
        return render(request, 'AppBlog/editarPost.html',{'formulario':formulario,'url':avatar[0].avatar.url, 'restaurante':restaurante})
    else:
        return render(request, 'AppBlog/index.html',{'mensaje':"Solo el administrador puede realizar esta accion",'url':avatar[0].avatar.url})

@login_required
def crearPost(request):
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user)
    if request.method == "POST":
        formulario = CrearRestaurante(request.POST,request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            restaurante = Restaurante(nombre = informacion['nombre'],direccion = informacion['direccion'],telefono = informacion['telefono'],calificacion = informacion['calificacion'] ,tipoDeComida = informacion['tipoDeComida'],categoriaPrecio = informacion['categoriaPrecio'],comentario = informacion['comentario'],autor = request.user,fecha = datetime.datetime.now(),imagen = informacion['imagen'])
            restaurante.save()
            return render (request, 'AppBlog/index.html', {'mensaje': 'Posteo creado exitosamente.', 'url':avatar[0].avatar.url })
    else:
        formulario = CrearRestaurante()
    return render(request, 'AppBlog/crearPost.html',{'url':avatar[0].avatar.url,'formulario':formulario})

@login_required
def mensajeria(request):
    avatar = Avatar.objects.filter(user=request.user)
    return render(request, 'mensajeria/mensajeria.html',{'url':avatar[0].avatar.url})

def about(request):
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user)
        return render(request, 'AppBlog/about.html',{'url':avatar[0].avatar.url})
    else:
        return render(request, 'AppBlog/about.html')