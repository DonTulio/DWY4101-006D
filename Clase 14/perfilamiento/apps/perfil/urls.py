from django.urls import path

from .views import registro, iniciar,salir,perfil
urlpatterns = [
    path('registro/',registro, name='registro'),
    path('',iniciar,name='iniciar'),
    path('salir/',salir,name='  '),
    path('perfil/',perfil,name='perfil')
]