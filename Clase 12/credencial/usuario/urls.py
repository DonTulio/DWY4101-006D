from django.urls import path

from .views import login, salir, registrar, perfil 

urlpatterns = [
    path('',login, name='login'),
    path('salir/',salir, name='salir'),
    path('registrar/',registrar, name='registrar'),
    path('perfil/',perfil, name='perfil')
]