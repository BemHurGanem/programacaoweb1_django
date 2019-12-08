from datetime import datetime

from django.db import models

# Create your models here.
class Produto(models.Model):

    nome = models.CharField(max_length=100, null=False, blank=False)
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.nome


class Venda(models.Model):

    data_venda = models.DateTimeField(default= datetime.now)
    cliente = models.OneToOneField(Cliente, on_delete=models.SET_NULL, null=True)
    produtos = models.ManyToManyField(Produto, through='ProdutosVenda')
    observacoes = models.CharField(max_length=300, null=False, blank=False)


class ProdutosVenda(models.Model):

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False)