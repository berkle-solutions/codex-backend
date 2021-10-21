from django.db import models
from codex.models.encomenda import Encomenda
from codex.models.compartilhamento import Compartilhamento


class EncomendaCompartilhamento(models.Model):
    encomenda = models.ForeignKey(Encomenda, on_delete=models.CASCADE)
    compartilhamento = models.ForeignKey(
        Compartilhamento, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
