from django import forms
from .models import Abastecimento


class AbastecimentoForm(forms.ModelForm):
    class Meta:
        model = Abastecimento
        fields = [
            'veiculo',
            'litros',
            'valor',
            'data',
            'tipo_combustivel',
        ]