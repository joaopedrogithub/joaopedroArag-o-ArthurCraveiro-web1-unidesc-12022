from django.db import models

# Create your models here.

class Locacao(models.Model):

    data_desocupacao = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    forma_garantia = models.CharField(max_length=100)
    fiador = models.CharField(max_length=100)
