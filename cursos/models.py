from django.db import models
from datetime import datetime

from usuarios.models import Usuario


class Cursos(models.Model):
    nome = models.CharField(max_length=100)
    # Upload de um texto
    descricao = models.TextField()
    # Upload de imagem a pasta thumb_cursos
    thumb = models.ImageField(upload_to="thumb_cursos")

    def __str__(self) -> str:
        return self.nome


class Aulas(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    # Upload para a pasta aulas
    aula = models.FileField(upload_to="aulas")
    # Fazer relação com o ID do curso
    curso = models.ForeignKey(Cursos, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome


class Comentarios(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    comentario = models.TextField()
    data = models.DateField(default=datetime.now)
    aula = models.ForeignKey(Aulas, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.usuario.nome


class NotasAulas(models.Model):
    # Uma lista com escolhas
    choices = (
        ('p', 'Péssimo'),
        ('r', 'Ruim'),
        ('re', 'Regular'),
        ('b', 'bom'),
        ('o', 'Ótimo')
    )

    aula = models.ForeignKey(Aulas, on_delete=models.DO_NOTHING)
    nota = models.CharField(max_length=50, choices=choices)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
