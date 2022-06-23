from django.db import models

# Create your models here.

class Deposito(models.Model):

    id_deposito = models.CharField(max_length=100)
