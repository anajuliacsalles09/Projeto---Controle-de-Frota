from django.db import models


class Abastecimento(models.Model):

    veiculo = models.ForeignKey(
        'veiculo.Veiculo',
        on_delete=models.CASCADE
    )

    litros = models.FloatField()
    valor = models.FloatField()
    data = models.DateField()
    tipo_combustivel = models.CharField(max_length=50)