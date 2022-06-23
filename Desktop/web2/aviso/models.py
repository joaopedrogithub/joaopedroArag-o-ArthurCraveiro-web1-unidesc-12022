from django.db import models

# Create your models here.

class Aviso(models.Model):

    matricula_avi = models.CharField(max_length=100)
    assunto_avi = models.CharField(max_length=100)
    data_avi = models.CharField(max_length=100)

    def __str__(self):
        return self.incluiraviso

    def __str__(self):
        return self.consultaraviso

    def __str__(self):
        return self.removeraviso

