from rest_framework import serializers
from codex.models.compartimento import Compartimento


class CompartimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compartimento
        fields = ["id", "descricao", "ocupado", "armario"]
