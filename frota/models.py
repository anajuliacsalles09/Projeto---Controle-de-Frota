from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.IntegerField()
    numero = models.IntegerField()
    logradouro = models.CharField(max_length=100)


class Viagem(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )
    origem = models.CharField(max_length=100)
    data_saida = models.DateField()
    data_retorno = models.DateField()
    destino = models.CharField(max_length=100)
    distancia = models.FloatField()
    valor_frete = models.FloatField()
    valor_resultado = models.FloatField()
    status = models.CharField(max_length=50)
