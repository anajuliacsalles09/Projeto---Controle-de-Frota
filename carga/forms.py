from django import forms
from .models import Carga


class CargaForm(forms.ModelForm):

    class Meta:
        model = Carga

        fields = [
            'viagem',
            'descricao',
            'peso',
            'valor',
            'observacao',
        ]

        widgets = {
            'viagem': forms.Select(attrs={
                'class': 'form-control'
            }),

            'descricao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição da carga'
            }),

            'peso': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Peso da carga'
            }),

            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Valor da carga'
            }),

            'observacao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Observações'
            }),
        }