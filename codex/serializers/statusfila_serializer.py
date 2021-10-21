from rest_framework import serializers
from codex.models.statusfila import StatusFila


class StatusFilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusFila
        fields = ['id', 'descricao']
