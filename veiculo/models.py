from django.db import models


class Veiculo(models.Model):
    placa = models.CharField(max_length=10)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    quilometragem = models.FloatField()
    status = models.CharField(max_length=50)
    capacidade_carga = models.FloatField()