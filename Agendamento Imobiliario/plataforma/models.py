from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Imagem(models.Model):
    img = models.ImageField(upload_to="img")

    def __str__(self) -> str:
        return self.img.url


class Cidade(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nome


class DiasVisita(models.Model):
    dia = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.dia


class Horario(models.Model):
    horario = models.TimeField()

    def __str__(self) -> str:
        return str(self.horario)


class Imovei(models.Model):
    choices = (("V", "Venda"), ("A", "Aluguel"))

    choices_imovel = (("A", "Apartamento"), ("C", "Casa"))

    imagens = models.ManyToManyField(Imagem)
    valor = models.FloatField()
    quartos = models.IntegerField()
    tamanho = models.FloatField()
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)
    rua = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=choices)
    tipo_imovel = models.CharField(max_length=1, choices=choices_imovel)
    numero = models.IntegerField()
    descricao = models.TextField()
    dias_visita = models.ManyToManyField(DiasVisita)
    horarios = models.ManyToManyField(Horario)

    def __str__(self) -> str:
        return self.rua


class Visitas(models.Model):
    choices = (
        ("S", "Segunda"),
        ("T", "Terça"),
        ("Q", "Quarta"),
        ("QI", "Quinta"),
        ("SE", "Sexta"),
        ("SA", "Sabado"),
        ("D", "Domingo"),
    )

    choices_status = (("A", "Agendado"), ("F", "Finalizado"), ("C", "Cancelado"))
    imovel = models.ForeignKey(Imovei, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dia = models.CharField(max_length=20)
    horario = models.TimeField()
    status = models.CharField(max_length=1, choices=choices_status, default="A")

    def __str__(self) -> str:
        return self.usuario.username
