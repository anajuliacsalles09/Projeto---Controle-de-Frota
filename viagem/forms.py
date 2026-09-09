from django import forms

from .models import Viagem


class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = [
            'usuario',
            'veiculo',
            'origem',
            'data_saida',
            'data_retorno',
            'destino',
            'distancia',
            'valor_frete',
            'valor_resultado',
            'status',
        ]