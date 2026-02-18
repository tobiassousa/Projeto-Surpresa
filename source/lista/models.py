from django.db import models


class Lista(models.Model):
    nome = models.CharField()
    relacao = models.CharField()
    confirmado = models.CharField()
    idade_menor = models.CharField(null=True, blank=True)
    idade_maio = models.CharField(null=True, blank=True)
    
    def __str__(self):
        return self.nome    