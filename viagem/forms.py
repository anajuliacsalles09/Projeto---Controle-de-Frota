
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

        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'veiculo': forms.Select(attrs={'class': 'form-control'}),
            'origem': forms.TextInput(attrs={'class': 'form-control'}),
            'data_saida': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_retorno': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'distancia': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_frete': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_resultado': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
