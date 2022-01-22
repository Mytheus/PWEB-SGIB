from django.db import models


class Livro(models.Model):

    GENEROS = (
        (0, "Nenhum"),
        (1, "Ação"),
        (2, "Aventura"),
        (3, "Clássicos"),
        (4, "Cultural"),
        (5, "Fantasia"),
        (6, "Ficção científica"),
        (7, "Poesia"),
        (8, "Contos"),
        (9, "Romance"),
        (10, "Terror"),
        (11, "Suspense"),
        (12, "Não ficção")
    )

    titulo = models.CharField(max_length=255)
    genero = models.IntegerField(choices=GENEROS, default=0)
    autor = models.CharField(max_length=255)
    editora = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    disponivel = models.BooleanField(default=True)
