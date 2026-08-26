from django.db import models


class Viagem(models.Model):

    usuario = models.ForeignKey(
        'usuario.Usuario',
        on_delete=models.CASCADE
    )

    veiculo = models.ForeignKey(
        'veiculo.Veiculo',
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