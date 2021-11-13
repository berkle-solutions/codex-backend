from django.db import models
from codex.models.armario import Armario


class Compartilhamento(models.Model):
    descricao = models.CharField(max_length=45)
    ocupado = models.BooleanField(default=False)
    armario = models.ForeignKey(Armario, related_name='compartimentos', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['armario', 'descricao']
        ordering = ['descricao']

    def __str__(self) -> str:
        return self.name        
