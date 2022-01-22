from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Usuário")
    password = forms.CharField(
        widget=forms.PasswordInput(), max_length=128, label="Senha")