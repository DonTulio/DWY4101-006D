from django.contrib import admin
from .models import Carrito,Producto,Categoria
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Carrito)