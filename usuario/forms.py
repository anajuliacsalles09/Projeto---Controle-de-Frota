
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class UsuarioForm(UserCreationForm):

    class Meta:
        model = Usuario

        fields = [
            'username',
            'nome',
            'email',
            'cpf',
            'telefone',
            'rua',
            'bairro',
            'cep',
            'numero',
            'logradouro',
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome de usuário',
            }),

            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome completo',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o e-mail',
            }),

            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000.000.000-00',
            }),

            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000',
            }),

            'rua': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a rua',
            }),

            'bairro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o bairro',
            }),

            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '00000-000',
            }),

            'numero': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número da residência',
            }),

            'logradouro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o logradouro',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for campo in self.fields.values():
            campo.widget.attrs.update({
                'class': 'form-control'
            })
