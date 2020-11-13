from django.shortcuts import render, redirect, reverse

def mostarPantallaComentario(request):
    return render(
        request,
        'comentario/index.html'
    )