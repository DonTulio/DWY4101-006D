from django.shortcuts import render
from django.contrib.auth.decorators import login_required
def ingreso(request):
    return render(
        request,
        'ingreso/index.html'
    )

@login_required
def perfil(request):
    return render(
        request,
        'ingreso/perfil.html'
    )