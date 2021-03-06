# Generated by Django 4.0.1 on 2022-01-22 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('genero', models.IntegerField(choices=[(0, 'Nenhum'), (1, 'Ação'), (2, 'Aventura'), (3, 'Clássicos'), (4, 'Cultural'), (5, 'Fantasia'), (6, 'Ficção científica'), (7, 'Poesia'), (8, 'Contos'), (9, 'Romance'), (10, 'Terror'), (11, 'Suspense'), (12, 'Não ficção')], default=0)),
                ('autor', models.CharField(max_length=255)),
                ('editora', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('disponivel', models.BooleanField(default=True)),
            ],
        ),
    ]
