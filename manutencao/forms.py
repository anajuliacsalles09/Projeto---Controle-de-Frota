from django import forms
from .models import Manutencao


class ManutencaoForm(forms.ModelForm):

    class Meta:
        model = Manutencao

        fields = [
            'veiculo',
            'tipo',
            'descricao',
            'data',
            'valor',
        ]

        widgets = {
            'veiculo': forms.Select(attrs={
                'class': 'form-control'
            }),

            'tipo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tipo de manutenção'
            }),

            'descricao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição da manutenção'
            }),

            'data': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Valor da manutenção'
            }),
        }