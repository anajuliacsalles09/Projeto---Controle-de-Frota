
from django import forms
from .models import Despesa


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa

        fields = [
            'viagem',
            'tipo',
            'descricao',
            'valor',
            'data',
        ]

        widgets = {
            'viagem': forms.Select(attrs={
                'class': 'form-control',
            }),

            'tipo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Pedágio, alimentação, hospedagem...',
            }),

            'descricao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe os detalhes da despesa',
            }),

            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0,00',
                'step': '0.01',
                'min': '0',
            }),

            'data': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }
