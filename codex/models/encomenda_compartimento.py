from django.db import models
from codex.models.encomenda import Encomenda
from codex.models.compartimento import Compartimento


class EncomendaCompartimento(models.Model):
    encomenda = models.ForeignKey(Encomenda, on_delete=models.CASCADE)
    compartimento = models.ForeignKey(
        Compartimento, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
