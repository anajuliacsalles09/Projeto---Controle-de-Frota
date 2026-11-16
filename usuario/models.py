
from django.db import models
from django.contrib.auth.models import User


class Usuario(User):

    TIPOS_USUARIO = [
        ('ADMIN', 'Administrador'),
        ('FUNCIONARIO', 'Funcionário'),
    ]

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)
    numero = models.IntegerField()
    logradouro = models.CharField(max_length=100)

    tipo = models.CharField(
        max_length=15,
        choices=TIPOS_USUARIO,
        default='FUNCIONARIO',
        verbose_name='Tipo de usuário'
    )

    def __str__(self):
        return self.nome
