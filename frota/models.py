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


class Veiculo(models.Model):
    placa = models.CharField(max_length=10)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    quilometragem = models.FloatField()
    status = models.CharField(max_length=50)
    capacidade_carga = models.FloatField()


class Abastecimento(models.Model):
    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.CASCADE
    )
    litros = models.FloatField()
    valor = models.FloatField()
    data = models.DateField()
    tipo_combustivel = models.CharField(max_length=50)


class Manutencao(models.Model):
    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.CASCADE
    )
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    data = models.DateField()
    valor = models.FloatField()

class Carga(models.Model):
    viagem = models.ForeignKey(
        Viagem,
        on_delete=models.CASCADE
    )
    descricao = models.CharField(max_length=255)
    peso = models.FloatField()
    valor = models.FloatField()
    observacao = models.CharField(max_length=255)


class Despesa(models.Model):
    viagem = models.ForeignKey(
        Viagem,
        on_delete=models.CASCADE
    )
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    valor = models.FloatField()
    data = models.DateField()