from rest_framework import serializers
from codex.models.fila_encomenda import FilaEncomenda


class FilaEncomendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilaEncomenda
        fields = ['id', 'data_entrada', 'data_saida', 'pessoa', 'status_fila', 'encomenda']
