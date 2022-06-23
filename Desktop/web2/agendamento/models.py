from django.db import models

# Create your models here.

class Agendamento(models.Model):

    dia = models.CharField(max_length=100)
    hora = models.CharField(max_length=100)
    local = models.CharField(max_length=100)

    def __str__(self):
        return self.incluir_agendamento

    def __str__(self):
        return self.consultar_agendamento

    def __str__(self):
        return self.alterar_agendamento

    def __str__(self):
        return self.remover_agendamento
