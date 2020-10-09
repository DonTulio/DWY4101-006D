from django.db import models

# Create your models here.
class  Producto(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    precio =  models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    detalle = models.TextField(max_length=150)
    fecha_creacion = models.DateTimeField(auto_now=True)
