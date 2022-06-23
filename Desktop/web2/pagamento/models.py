from django.db import models

# Create your models here.

class Pagamento(models.Model):

    valor_pag = models.CharField(max_length=100)
    forma_pag = models.CharField(max_length=100)
    parcelas_pag = models.CharField(max_length=100)
    data_pag = models.CharField(max_length=100)
    banco_pag = models.CharField(max_length=100)
    agencia_pag = models.CharField(max_length=100)
    conta_pag = models.CharField(max_length=100)