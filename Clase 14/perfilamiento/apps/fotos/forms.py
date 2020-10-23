from django import forms
from .models import Foto
class FormFotos(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ('titulo','foto','detalle')