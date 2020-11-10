from django.db import models

# Create your models here.
class Comentario(models.Model):
    titulo = models.CharField(max_length= 45, blank=False)
    comentario = models.TextField(blank=False)
    fecha = models.DateTimeField(auto_now = True)
