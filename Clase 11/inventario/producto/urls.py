from django.urls import path

from .views import agregarProducto, listarProducto, modificarProducto, eliminarProducto

urlpatterns = [
    path('',listarProducto, name='listar_producto'),
    path('agregar/',agregarProducto, name='agregar_producto'),
    path('editar/<int:id_producto>',modificarProducto,name='modificar_producto'),
    path('eliminar/<int:id_producto>',eliminarProducto, name='eliminar_producto')
]