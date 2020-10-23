from django.urls import path
from .views import agregarFoto
urlpatterns = [
    path('agregar/',agregarFoto, name='agregarFoto')
]