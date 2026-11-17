
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


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
    km_saida = models.DecimalField('Quilometragem de saída (km)', max_digits=12, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])
    km_chegada = models.DecimalField('Quilometragem de chegada (km)', max_digits=12, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])
    valor_frete = models.FloatField()
    valor_resultado = models.FloatField(default=0, editable=False)
    status = models.CharField(max_length=50)

    def calcular_resultado(self):
        from despesa.models import Despesa
        total_despesas = Despesa.calcular_total(self) if self.pk else 0
        return round(self.valor_frete - total_despesas, 2)

    def clean(self):
        super().clean()
        if self.km_saida is not None and self.km_chegada is None:
            raise ValidationError({'km_chegada': 'Informe a quilometragem de chegada.'})
        if self.km_chegada is not None and self.km_saida is None:
            raise ValidationError({'km_saida': 'Informe a quilometragem de saída.'})
        if self.km_saida is not None and self.km_chegada is not None:
            if self.km_chegada < self.km_saida:
                raise ValidationError({'km_chegada': 'A quilometragem de chegada deve ser maior ou igual à de saída.'})
            self.distancia = float(self.km_chegada - self.km_saida)

    def save(self, *args, **kwargs):
        self.valor_resultado = self.calcular_resultado()
        if kwargs.get('update_fields') is not None:
            kwargs['update_fields'] = set(kwargs['update_fields']) | {'valor_resultado'}
        if self.km_saida is not None and self.km_chegada is not None:
            self.distancia = float(self.km_chegada - self.km_saida)
            if kwargs.get('update_fields') is not None:
                kwargs['update_fields'] = set(kwargs['update_fields']) | {'distancia'}
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.origem} - {self.destino}'
