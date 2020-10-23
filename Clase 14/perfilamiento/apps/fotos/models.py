from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Foto(models.Model):
    titulo = models.CharField(max_length=45, blank=False)
    foto = models.FileField(upload_to='fotos')
    detalle = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)