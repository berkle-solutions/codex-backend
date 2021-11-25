from django.db import models
from codex.models.encomenda import Encomenda
from codex.models.pessoa import Pessoa
from codex.models.statusfila import StatusFila
from datetime import datetime

class FilaEncomenda(models.Model):
    data_entrada = models.DateTimeField(null=True, blank=True, default=datetime.now)
    data_saida = models.DateTimeField(null=True, blank=True, default=datetime.now)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    status_fila = models.ForeignKey(StatusFila, on_delete=models.CASCADE)
    encomenda = models.ForeignKey(Encomenda, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
