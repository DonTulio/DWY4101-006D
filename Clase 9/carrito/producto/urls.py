from django.urls import path
from .views import saludar, agregar, modificar, calcular,calcularDosNumeros

urlpatterns = [
    path("saludar/",saludar),
    path("agregar/",agregar),
    path("modificar/",modificar),
    path("calcular/<valor1>", calcular),
    path("calcular/<int:valor1>/<int:valor2>", calcularDosNumeros)
]