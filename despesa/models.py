from django.db import models


class Despesa(models.Model):

    viagem = models.ForeignKey(
        'viagem.Viagem',
        on_delete=models.CASCADE
    )

    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    valor = models.FloatField()
    data = models.DateField()