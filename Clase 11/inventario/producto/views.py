from django.shortcuts import render, redirect

from .models import Producto
from .forms import ProductoForm

# Create your views here.
def listarProducto(request):
    productos = Producto.objects.all()
    context = {
        'titulo':'Listar producto',
        'productos':productos
    }
    return render(
        request,
        'producto/listar_producto.html',
        context
    )

def agregarProducto(request):
    formulario = None
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/producto/')
    else:
        formulario = ProductoForm()
    context = {
        'titulo':'Agregar producto',
        'formulario':formulario
    }
    return render(
        request,
        'producto/agregar_producto.html',
        context
    )

def modificarProducto(request,id_producto):
    producotoEncontrado = Producto.objects.get(pk=id_producto)
    formulario = None
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producotoEncontrado)
        if formulario.is_valid():
            formulario.save()
            return redirect('/producto/')
    else:
        formulario = ProductoForm(instance=producotoEncontrado)
    context = {
        'titulo':'Modificar producto',
        'formulario':formulario
    }
    return render(
        request,
        'producto/modificar_producto.html',
        context
    )

def eliminarProducto(request,id_producto):
    productoEncontrado = Producto.objects.get(pk = id_producto)
    productoEncontrado.delete()
    return redirect('/producto/')