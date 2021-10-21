from django.db import models


class StatusFila(models.Model):
    descricao = models.CharField(max_length=45)

    def __str__(self):
        return self.name
