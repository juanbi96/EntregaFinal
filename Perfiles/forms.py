from django import forms

class PerfilForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    imagen = forms.ImageField()
    link = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=500)
    email = forms.EmailField()
    contraseña = forms.CharField(max_length=30)