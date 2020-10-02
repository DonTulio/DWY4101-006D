from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludar(request):
    return HttpResponse("Hola mundo! desde Django")

def agregar(request):
    return HttpResponse("Agregar nuevo producto")

def modificar(request):
    return HttpResponse("Modificar nuevo producto")

def calcular(request, valor1):
    resultado = "El valor ingresado es {}"
    return HttpResponse(resultado.format(valor1))

def calcularDosNumeros(request, valor1, valor2):
    resultado = valor1 + valor2
    return HttpResponse("""
        <h1>El resultado es</h1>
        <p>{}</p>
    """.format(resultado))