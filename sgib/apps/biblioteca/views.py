from django.http import Http404
from django.shortcuts import render, redirect
from sgib.apps.biblioteca.forms import LivroForm
from sgib.apps.biblioteca.models import Livro
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def livros(request):
    context = {}
    context['form'] = LivroForm()
    if request.method == "POST":
        form = LivroForm(request.POST or None)

        if form.is_valid():
            form.save(commit=True)
        else:
            context['form'] = form
        
    
    livros = Livro.objects.all()

    context['livros'] = []
    for livro in livros:
        context['livros'].append(
            {
                "id": livro.id,
                "titulo": livro.titulo,
                "genero": livro.get_genero_display(),
                "autor": livro.autor,
                "editora": livro.editora,
                "descricao": livro.descricao,
                "disponivel": "Sim" if livro.disponivel else "Não"
            }
        )

    return render(request, 'booklist.html', context)


def deletar_livro(request, id):
    try:
        livro = Livro.objects.get(id=id)
    
    except Livro.DoesNotExist:
        raise Http404

    livro.delete()

    return redirect('livros')
