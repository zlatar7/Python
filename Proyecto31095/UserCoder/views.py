from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm # UserCreationForm 
from django.contrib.auth.decorators import login_required 

from UserCoder.forms import *
from UserCoder.models import *

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user.has_usable_password:
                login(request, user)
                redirect( 'AppCoderInicio')
            else:
                redirect('UserCoderLogin')
               
        else:
                redirect('UserCoderLogin')

        return redirect('UserCoderLogin')

    contexto = {
        'form': AuthenticationForm(),
        'nombre_form': 'LOGIN'
    }
    return render(request, 'UserCoder/login.html', contexto)

def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no pudo ser registrado!')
        return redirect('AppCoderInicio')

    contexto = {
        # 'form': UserCreationForm(),
        'form': UserRegisterForm(),
        'boton_envio': 'REGISTRARSE'
    }

    return render(request, 'base_formulario.html', contexto)

def info(request):

    return render(request, 'UserCoder/sesion_fallida.html')

@login_required

def editar_usuario(request):

    usuario = request.user

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            usuario.username = data.get('username')
            usuario.email = data.get('email')
            usuario.last_name = data.get('last_name')

            usuario.save()

            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no pudo ser registrado!')
        
        return redirect('AppCoderInicio')

    contexto = {
    'form': UserRegisterForm(
        initial={
            'username': usuario.username,
            'email': usuario.email,
            'last_name': usuario.last_name
        }),
    'boton_envio': 'REGISTRARSE'
    }

    return render(request, 'base_formulario.html', contexto)

def upload_avatar(request):
    if request.method == "POST":

        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            avatar = Avatar.objects.filter(user=data.get("usuario"))

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=data.get("user"), imagen=data.get("imagen"))
                avatar.save()

        return redirect("AppCoderInicio")

    contexto = {
        "form": AvatarForm(),
        'boton_envio': 'Crear'
    }
    return render(request, "base_formulario.html", contexto)