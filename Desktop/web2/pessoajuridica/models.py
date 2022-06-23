from django.db import models

# Create your models here.

class Pessoajuridica(models.Model):

    cnpj = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    representante_legal = models.CharField(max_length=100)
