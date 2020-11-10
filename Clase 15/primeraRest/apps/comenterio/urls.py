from django.urls import path
from .views import saludar,buscarEliminarActualizar,listarAgregarBorrarTodoXD
"""
    Yo tengo cometnarios, debo acceder a ellos, guardarlos, modificarlos y eliminarlos
    ¿Por donde lo realizaré?
    http:localhost/api/comentarios/
    POST   = CREAR
    GET    = LISTAR
    DELETE = BORRAR
    http:localhost/api/comentarios/pk=valor
    GET    = BUSCAR UN COMENTARIO
    PUT    = MODIFICAR UN COMENTARIO POR ID
    DELETE = BORRAR UN COMENTARIO POR ID
"""

urlpatterns = [
    path('saludar/',saludar,name="saludar"),
    path('comentario/',listarAgregarBorrarTodoXD),
    path('comentario/<int:id>/',buscarEliminarActualizar)
]