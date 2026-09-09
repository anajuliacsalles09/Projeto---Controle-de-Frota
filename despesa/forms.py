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