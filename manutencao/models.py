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

    @classmethod
    def consultar_historico(cls, veiculo=None):
        historico = cls.objects.all()
        if veiculo is not None:
            historico = historico.filter(veiculo=veiculo)
        return historico.order_by('-data', '-pk')
