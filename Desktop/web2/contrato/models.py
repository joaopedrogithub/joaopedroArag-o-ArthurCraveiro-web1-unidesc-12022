from django.db import models

# Create your models here.

class Contrato(models.Model):

    dados_cliente = models.CharField(max_length=100)
    dados_corretor = models.CharField(max_length=100)
    descricao_imovel = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    documentacao = models.CharField(max_length=100)
    clausula_penal = models.CharField(max_length=100)

