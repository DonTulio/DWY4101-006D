from django.shortcuts import render,redirect
from .forms import FormFotos
# Create your views here.
def agregarFoto(request):
    formulario = FormFotos()
    if request.method == 'POST':
        formulario = FormFotos(request.POST, request.FILES)
        if formulario.is_valid():
            nuevoFormulario = formulario.save(commit=False)
            nuevoFormulario.usuario = request.user
            nuevoFormulario.save()
            return redirect('/perfil/')
    context = {
        'formulario':formulario
    }
    return render(
        request,
        'fotos/agregar.html',
        context
    )
        