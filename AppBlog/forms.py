from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm,forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm,forms.Form):
    email = forms.EmailField(label='Modificar Mail',required=False)
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput,required=False)
    password2 = forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput,required=False)
    last_name = forms.CharField(label='Modificar Apellido',required=False)
    first_name = forms.CharField(label='Modificar Nombre',required=False)
    class Meta:
        model = User
        fields = ('email','password1','password2','last_name','first_name')
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    avatar = forms.ImageField(label='Avatar')

class CrearRestaurante(forms.Form):
    nombre = forms.CharField(label='nombre del local')
    direccion = forms.CharField(label='Direccion del local')
    telefono = forms.IntegerField(label='Telefono del local',required=False)
    calificacion = forms.IntegerField(label='Calificacion',required=False)
    tipoDeComida = forms.CharField(label='Tipo de comida')
    categoriaPrecio = forms.CharField(label='Precios')
    comentario = forms.CharField(label='Que te parecio el lugar?',required=False,widget=forms.Textarea)
    imagen = forms.ImageField(label='Imagen')

class EditPost(forms.Form):
    direccion = forms.CharField(label='Direccion del local',required=False)
    telefono = forms.IntegerField(label='Telefono del local',required=False)
    calificacion = forms.IntegerField(label='Calificacion',required=False)
    comentario = forms.CharField(label='Que te parecio el lugar?',required=False,widget=forms.Textarea)

