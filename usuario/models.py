
from django.db import models
from django.contrib.auth.models import User


class Usuario(User):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.IntegerField()
    numero = models.IntegerField()
    logradouro = models.CharField(max_length=100)