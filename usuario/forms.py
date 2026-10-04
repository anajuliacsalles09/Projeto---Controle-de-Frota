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