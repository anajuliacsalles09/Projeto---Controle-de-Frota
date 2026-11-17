
from django import forms
from .models import Viagem


class ViagemForm(forms.ModelForm):
    distancia = forms.FloatField(label='Distância percorrida (km)', required=False, disabled=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        help_text='Calculada ao salvar: quilometragem de chegada menos quilometragem de saída.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        legacy = self.instance.pk and self.instance.km_saida is None and self.instance.km_chegada is None
        for name in ('km_saida', 'km_chegada'):
            self.fields[name].required = not legacy
        self.fields['km_saida'].help_text = 'Leitura do painel do veículo antes de sair.'
        self.fields['km_chegada'].help_text = 'Leitura do painel após retornar. Inclui ida e volta.'
        if legacy:
            self.fields['distancia'].help_text += ' Viagem antiga: preencha as duas leituras para recalcular ou deixe ambas vazias para manter a distância registrada.'

    class Meta:
        model = Viagem

        fields = [
            'usuario',
            'veiculo',
            'origem',
            'data_saida',
            'data_retorno',
            'destino',
            'km_saida',
            'km_chegada',
            'distancia',
            'valor_frete',
            'status',
        ]

        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'veiculo': forms.Select(attrs={'class': 'form-control'}),
            'origem': forms.TextInput(attrs={'class': 'form-control'}),
            'data_saida': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'data_retorno': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'destino': forms.TextInput(attrs={'class': 'form-control'}),
            'km_saida': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
            'km_chegada': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
            'valor_frete': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
