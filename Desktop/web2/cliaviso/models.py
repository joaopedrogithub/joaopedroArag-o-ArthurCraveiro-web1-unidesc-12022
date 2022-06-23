from django.db import models

# Create your models here.


class Cliaviso(models.Model):

    mensagem = models.CharField(max_length=100)