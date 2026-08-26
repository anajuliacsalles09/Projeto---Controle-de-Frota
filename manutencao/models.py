from django.db import models


class Manutencao(models.Model):

    veiculo = models.ForeignKey(
        'veiculo.Veiculo',
        on_delete=models.CASCADE
    )

    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    data = models.DateField()
    valor = models.FloatField()