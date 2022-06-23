from django.db import models

# Create your models here.

class Cliente(models.Model):

    data_cadastro = models.CharField(max_length=100)

    def __str__(self):
        return self.consultar_imoveis

    def __str__(self):
        return self.manter_conta

    def __str__(self):
        return self.agendar_visita
