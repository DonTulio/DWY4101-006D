from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=50, blank=False)
    precioProducto = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        nombre = "{} {}"
        return nombre.format(self.nombreProducto,self.precioProducto)

class Carrito(models.Model):
    productos = models.ForeignKey(Producto, on_delete = models.CASCADE)
    fechaCompra = models.DateField(auto_now=True)
    cantidad = models.PositiveIntegerField()


