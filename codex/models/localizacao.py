from django.db import models
from codex.models.pessoa import Pessoa


class Localizacao(models.Model):
    bloco = models.CharField(max_length=45)
    andar = models.CharField(max_length=45)
    unidade = models.CharField(max_length=45)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
