from django import forms


class NuevoPost(forms.Form):
    titulo = forms.CharField(max_length=60)
    subtitulo = forms.CharField(max_length=120)
    cuerpo = forms.CharField(max_length=1000)
    autor = forms.CharField(max_length=30)
    fecha = forms.DateField()
    imagen = forms.ImageField()
