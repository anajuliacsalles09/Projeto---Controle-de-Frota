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