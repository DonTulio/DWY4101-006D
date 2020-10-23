from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import FormCreacionUsuario, FormCreacionPerfil, FormIniciarSesion
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Genero,PerfilUser
from django.contrib.auth.models import User
from django.contrib import messages
from apps.fotos.models import Foto
# Create your views here.
def registro(request):
    formulario = FormCreacionUsuario()
    formulario2 = FormCreacionPerfil()
    if request.method == 'POST':
        formulario = FormCreacionUsuario(request.POST)
        formulario2 = FormCreacionPerfil(request.POST)
        if formulario.is_valid() and formulario2.is_valid():
            usuario = formulario.save()
            perfil = formulario2.save(commit=False)
            perfil.usuario = usuario
            perfil.save()
            messages.add_message(request,
                messages.INFO,
                'Registrado correctamente...')
            return redirect('/')
    # caso contrario es GET
    context = {
        'formulario':formulario,
        'formulario2': formulario2
    }
    return render(
        request,
        'usuario/registro.html',
        context
    )

def iniciar(request):
    formulario = FormIniciarSesion()
    if request.method == 'POST':
        formulario = FormIniciarSesion(data= request.POST)
        if formulario.is_valid():
            print("form valido")
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            usuarioEncontrado = authenticate(username=username, password = password)
            if usuarioEncontrado is not None:
                messages.add_message(
                    request,
                    messages.INFO,
                    "Bienvenido {}".format(usuarioEncontrado.get_username())
                )
                login(request,usuarioEncontrado)
                return redirect('/perfil/')
    context = {
        'formulario':formulario
    }
    return render(
        request,
        'usuario/inicio.html',
        context
    )

def salir(request):
    logout(request)
    return redirect('/')

def perfil(request):
    fotos = Foto.objects.all()
    context = {
        'fotos':fotos
    }
    return render(
        request,
        'usuario/perfil.html',
        context
    )