from rest_framework import serializers
from codex.models.encomenda_compartimento import EncomendaCompartimento
from codex.serializers.encomenda_serializer import EncomendaSerializer
from codex.serializers.compartimento_serializer import CompartimentoSerializer


class EncomendaCompartimentoSerializer(serializers.ModelSerializer):
    encomenda = EncomendaSerializer(many=False, read_only=True)
    compartimento = CompartimentoSerializer(many=False, read_only=True)
    class Meta:
        model = EncomendaCompartimento
        fields = ['id', 'encomenda', 'compartimento']