from django.db import models
from codex.models.pessoa import Pessoa


class Encomenda(models.Model):
    codigo_resgate: models.CharField(max_length=45)
    descricao: models.CharField(max_length=100)
    unidade: models.CharField(max_length=45)
    pessoa_id: models.ForeignKey(Pessoa, on_delete=models.CASCADE)
        
    class Meta:
        db_table = 'encomenda'
        app_label= 'encomenda'