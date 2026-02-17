from django.db import models


class Lista(models.Model):
    nome = models.CharField()
    relacao = models.CharField()
    confirmado = models.CharField()
    
    def __str__(self):
        return self.nome    