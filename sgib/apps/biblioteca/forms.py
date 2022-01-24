from django import forms
from sgib.apps.biblioteca.models import Livro

class LivroForm(forms.ModelForm):
    titulo = forms.CharField(label="Título*")
    autor = forms.CharField(label="Autor*")
    editora = forms.CharField(label="Editora*")
    disponivel = forms.CheckboxInput()

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'genero', 'autor', 'editora', 'descricao', 'disponivel'] 

        forms.widgets = {
          'titulo' : forms.TextInput(attrs={'class' : 'form-control'}),
          'genero' : forms.Select(attrs={'class' : 'form-control'}),
          'autor' : forms.TextInput(attrs={'class' : 'form-control'}),
          'editora' : forms.TextInput(attrs={'class' : 'form-control'}),
          'descricao' : forms.Textarea(attrs={'class' : 'form-control','id': 'inputDescription'}),
          'disponivel' : forms.CheckboxInput(attrs={'class' : 'form-control'})
        }