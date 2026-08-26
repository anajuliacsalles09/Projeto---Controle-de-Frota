from django.db import models


class Carga(models.Model):

    viagem = models.ForeignKey(
        'viagem.Viagem',
        on_delete=models.CASCADE
    )

    descricao = models.CharField(max_length=255)
    peso = models.FloatField()
    valor = models.FloatField()
    observacao = models.CharField(max_length=255)
