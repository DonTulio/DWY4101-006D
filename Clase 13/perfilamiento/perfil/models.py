from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Genero(models.Model):
    detalleNombre = models.CharField(max_length=45, blank=False)

class PerfilUser(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    
# @receiver(post_save,sender=User)
# def crearPerfilUsuario(sender,instance,created,**kwargs):
#     if created:
#         PerfilUser.objects.create(usuario=instance)

# @receiver(post_save, sender=User)
# def crearPerfilUsuario(sender, instance,**kwargs):
#     instance.usuario.save()
