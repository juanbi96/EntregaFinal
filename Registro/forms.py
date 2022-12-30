from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repita la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}
