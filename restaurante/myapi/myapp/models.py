from django.db import models

class Item(models.Model):

    titulo = models.CharField(primary_key=True, max_length=100)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(decimal_places=2, max_digits=5)
    classificacao = models.CharField(max_length=20)

class Adicional(models.Model):

    nome = models.CharField(primary_key=True, max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=5)
