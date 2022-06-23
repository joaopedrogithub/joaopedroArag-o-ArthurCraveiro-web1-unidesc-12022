from django.db import models

# Create your models here.

class Transferencia(models.Model):

    Tipo = models.CharField(max_length=100)
    cod_identificacao = models.CharField(max_length=100)