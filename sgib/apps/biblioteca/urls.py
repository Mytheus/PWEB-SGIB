from django.urls import path
from sgib.apps.biblioteca import views

urlpatterns = [
    path('', views.livros, name="livros"),
    path('<int:id>/', views.deletar_livro, name="delete-livro")
]