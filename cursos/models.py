from django.db import models

class Cursos(models.Model):
    nome = models.CharField(max_length = 100)
    # Upload de um texto
    descricao = models.TextField()
    # Upload de imagem a pasta thumb_cursos
    thumb = models.ImageField(upload_to = "thumb_cursos")

    def __str__(self) -> str:
        return self.nome

class Aulas(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    # Upload para a pasta aulas
    aula = models.FileField(upload_to = "aulas")
    # Fazer relação com o ID do curso
    curso = models.ForeignKey(Cursos, on_delete = models.DO_NOTHING)


    def __str__(self) -> str:
        return self.nome