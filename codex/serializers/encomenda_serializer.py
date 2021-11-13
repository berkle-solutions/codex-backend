from rest_framework import serializers
from codex.models.encomenda import Encomenda


class EncomendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encomenda
        fields = ['id', 'codigo_resgate', 'descricao', 'unidade', 'pessoa']
