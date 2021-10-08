from django.db import models


class Usuario(models.Model):
    # Criar um modelo seguindo certos dados
    # Char de string
    nome = models.CharField(max_length=50)

    # Char de email
    email = models.EmailField()

    senha = models.CharField(max_length=64)

    # Definir o nome de exibição como nome
    def __str__(self):
        return self.nome
