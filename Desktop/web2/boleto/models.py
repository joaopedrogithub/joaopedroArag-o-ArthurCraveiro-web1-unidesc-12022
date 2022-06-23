from django.db import models

# Create your models here.
class Boleto(models.Model):
    cod_cliente = models.CharField(max_length=100)
    nome_cliente = models.CharField(max_length=100)

