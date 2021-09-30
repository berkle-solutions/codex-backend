from django.db import models

class Perfil(models.Model):
    descricao: models.CharField(max_length=45)
    
    class Meta:
        db_table = 'perfil'
        app_label= 'perfil'