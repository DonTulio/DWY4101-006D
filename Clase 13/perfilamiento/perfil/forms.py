from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PerfilUser

class FormCreacionUsuario(UserCreationForm):
    genero = forms.Select()

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
    # def save(self, commit=True):
    #     if not commit:
    #         raise NotImplementedError('El usuario no se puede guarda en la base de datos.....')
    #     usuarioNuevo = super(FormCreacionPerfil,self).save(commit=True)
    #     perfilUser = PerfilUser(usuario=usuarioNuevo, genero=self.cleaned_data['genero'])
    #     perfilUser.save()
    #     return usuarioNuevo, perfilUser

class FormCreacionPerfil(forms.ModelForm):
    class Meta:
        model= PerfilUser
        fields= ('genero',)