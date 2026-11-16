
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


class UsuarioRegistroForm(UserCreationForm):
    """
    Formulário para cadastro público de funcionários.
    O usuário não pode escolher o próprio tipo de acesso.
    """

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

        labels = {
            'username': 'Nome de usuário',
            'nome': 'Nome completo',
            'email': 'E-mail',
            'cpf': 'CPF',
            'telefone': 'Telefone',
            'rua': 'Rua',
            'bairro': 'Bairro',
            'cep': 'CEP',
            'numero': 'Número',
            'logradouro': 'Logradouro',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome de usuário',
            }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome completo',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu e-mail',
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
                'placeholder': 'Digite sua rua',
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu bairro',
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

        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme sua senha'

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Digite novamente sua senha',
        })

    def save(self, commit=True):
        usuario = super().save(commit=False)

        # Cadastros públicos sempre começam como funcionários.
        usuario.tipo = 'FUNCIONARIO'
        usuario.is_staff = False
        usuario.is_superuser = False

        if commit:
            usuario.save()

        return usuario


class UsuarioForm(UserCreationForm):
    """
    Formulário utilizado pelo administrador para cadastrar usuários
    e definir o tipo de acesso.
    """

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
            'tipo',
        ]

        labels = {
            'username': 'Nome de usuário',
            'nome': 'Nome completo',
            'email': 'E-mail',
            'cpf': 'CPF',
            'telefone': 'Telefone',
            'rua': 'Rua',
            'bairro': 'Bairro',
            'cep': 'CEP',
            'numero': 'Número',
            'logradouro': 'Logradouro',
            'tipo': 'Tipo de usuário',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'rua': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'numero': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'logradouro': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme sua senha'

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
        })

    def save(self, commit=True):
        usuario = super().save(commit=False)

        # Administrador recebe acesso ao painel administrativo.
        usuario.is_staff = usuario.tipo == 'ADMIN'

        # Não transforma automaticamente o usuário em superusuário.
        # As permissões devem ser atribuídas conforme a configuração
        # de permissões do projeto.
        usuario.is_superuser = False

        if commit:
            usuario.save()

        return usuario


class UsuarioUpdateForm(forms.ModelForm):
    """
    Formulário para edição dos dados de um usuário existente.
    """

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
            'tipo',
        ]

        labels = {
            'username': 'Nome de usuário',
            'nome': 'Nome completo',
            'email': 'E-mail',
            'cpf': 'CPF',
            'telefone': 'Telefone',
            'rua': 'Rua',
            'bairro': 'Bairro',
            'cep': 'CEP',
            'numero': 'Número',
            'logradouro': 'Logradouro',
            'tipo': 'Tipo de usuário',
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'rua': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'numero': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'logradouro': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

    def save(self, commit=True):
        usuario = super().save(commit=False)

        usuario.is_staff = usuario.tipo == 'ADMIN'

        if commit:
            usuario.save()

        return usuario