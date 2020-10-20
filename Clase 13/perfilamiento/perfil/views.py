from django.shortcuts import render, redirect

from .forms import FormCreacionUsuario, FormCreacionPerfil
from django.contrib import messages
from .models import Genero,PerfilUser
from django.contrib.auth.models import User
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
    