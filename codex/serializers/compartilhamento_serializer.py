from rest_framework import serializers
from codex.models.compartilhamento import Compartilhamento


class CompartilhamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compartilhamento
        fields = ['id', 'descricao', 'ocupado', 'armario']