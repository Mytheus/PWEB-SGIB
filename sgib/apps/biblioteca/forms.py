from django import forms
from sgib.apps.biblioteca.models import Livro

class LivroForm(forms.ModelForm):
    titulo = forms.CharField(label="Título*")
    genero = forms.CharField(label='Genero*', widget=forms.Select(choices=Livro.GENEROS))
    autor = forms.CharField(label="Autor*")
    editora = forms.CharField(label="Editora*")
    descricao = forms.CharField(label="Descrição")
    disponivel = forms.CheckboxInput()

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'editora', 'descricao', 'disponivel']