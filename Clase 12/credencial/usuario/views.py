from django.shortcuts import render
from django.contrib.auth import login as entrar, logout as salir, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def login(request):
    formulario = None
    if request.method == 'POST':
        formulario = AuthenticationForm( data = request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contra = formulario.cleaned_data['password']
            usuarioLogeado = authenticate(username=usuario,password=contra)
            if usuarioLogeado is not None:
                entrar(request,usuarioLogeado)
    formulario = AuthenticationForm()
    context = {
        'form':formulario
    }
    return render(
        request,
        'usuario/login.html',
        context
    )

def salir(request):

def registrar(request):

def perfil(request):
