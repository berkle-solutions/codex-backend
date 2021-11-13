from django.db import models


class Armario(models.Model):
    descricao = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.name
