from django.db import models

# Create your models here.

class Funcionario(models.Model):

    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    data_nascimento = models.CharField(max_length=100)
    carteira_trabalho = models.CharField(max_length=100)
    salario = models.CharField(max_length=100)
    pis = models.CharField(max_length=100)

    def __str__(self):
        return self.consultar_imoveis

    def __str__(self):
        return self.manter_anuncio

    def __str__(self):
        return self.manter_cliente

    def __str__(self):
        return self.manter_funcionario

    def __str__(self):
        return self.manter_agendamento

    def __str__(self):
        return self.gerar_relatorio

    def __str__(self):
        return self.calcular_salario

