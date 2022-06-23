from django.db import models

# Create your models here.

class Fun_aviso(models.Model):

    mensagem = models.CharField(max_length=100)
