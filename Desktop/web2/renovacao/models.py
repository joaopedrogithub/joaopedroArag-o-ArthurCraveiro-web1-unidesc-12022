from django.db import models

# Create your models here.

class Renocacao(models.Model):

    data_desocupacao = models.CharField(max_length=100)
    data_renovacao = models.CharField(max_length=100)
    cartorio = models.CharField(max_length=100)
