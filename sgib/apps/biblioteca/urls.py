from django.urls import path
from sgib.apps.biblioteca import views

urlpatterns = [
    path('', views.index, name="index"),
    path('adicionar/', views.adicionar_livro, name="adicionar-livro"),
    path('<int:id>/', views.deletar_livro, name="delete-livro"),
    path('listar/', views.listar_livros, name="listar-livros")
]