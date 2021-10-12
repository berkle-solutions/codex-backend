from django.db import models
from codex.models.armario import Armario


class Compartilhamento(models.Model):
    descricao = models.CharField(max_length=45)
    ocupado = models.BooleanField(default=False)
    armario = models.ForeignKey(Armario, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
