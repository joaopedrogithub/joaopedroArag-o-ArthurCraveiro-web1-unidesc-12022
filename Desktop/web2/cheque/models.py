from django.db import models

# Create your models here.

class Cheque(models.Model):

    financeira = models.CharField(max_length=100)
    nome_cliente = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    data_abertura = models.CharField(max_length=100)
