from django.db import models
from codex.models.perfil import Perfil

class Pessoa(models.Model):
    nome= models.CharField(max_length=100)
    email= models.CharField(max_length=256)
    senha= models.CharField(max_length=256)
    cpf= models.CharField(max_length=11)
    data_nascimento= models.DateTimeField()
    telefone= models.CharField(max_length=12)
    celular= models.CharField(max_length=13)
    ativo= models.BooleanField(default='1', blank=False)
    perfil= models.ForeignKey(Perfil, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    