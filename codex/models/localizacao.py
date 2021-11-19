from django.db import models
from codex.models.pessoa import Pessoa


class Localizacao(models.Model):
    bloco = models.CharField(max_length=45, blank=True)
    andar = models.CharField(max_length=45, blank=True)
    unidade = models.CharField(max_length=45, blank=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name
