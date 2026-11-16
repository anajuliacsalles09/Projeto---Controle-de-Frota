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

        widgets = {
            'veiculo': forms.Select(attrs={
                'class': 'form-control'
            }),

            'litros': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Quantidade de litros'
            }),

            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Valor do abastecimento'
            }),

            'data': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'tipo_combustivel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Gasolina, Diesel ou Etanol'
            }),
        }