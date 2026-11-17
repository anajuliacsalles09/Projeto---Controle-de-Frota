from django.db import models
from django.db.models import Sum
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver


class Despesa(models.Model):

    viagem = models.ForeignKey(
        'viagem.Viagem',
        on_delete=models.CASCADE
    )

    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    valor = models.FloatField()
    data = models.DateField()

    @classmethod
    def calcular_total(cls, viagem=None):
        despesas = cls.objects.all()
        if viagem is not None:
            despesas = despesas.filter(viagem=viagem)
        return round(despesas.aggregate(total=Sum('valor'))['total'] or 0, 2)


@receiver(pre_save, sender=Despesa)
def guardar_viagem_anterior(sender, instance, **kwargs):
    if kwargs.get('raw'):
        return
    instance._viagem_anterior = sender.objects.filter(pk=instance.pk).values_list('viagem_id', flat=True).first()


@receiver(post_save, sender=Despesa)
@receiver(post_delete, sender=Despesa)
def atualizar_resultado_viagens(sender, instance, **kwargs):
    if kwargs.get('raw'):
        return
    from viagem.models import Viagem
    # Também atualiza a viagem antiga se a despesa mudar de viagem.
    ids = {instance.viagem_id, getattr(instance, '_viagem_anterior', None)}
    for viagem in Viagem.objects.filter(pk__in=ids):
        Viagem.objects.filter(pk=viagem.pk).update(valor_resultado=viagem.calcular_resultado())
