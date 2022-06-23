from django.db import models

# Create your models here.

class Pessoafisica(models.Model):

    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    data_nascimento = models.CharField(max_length=100)
