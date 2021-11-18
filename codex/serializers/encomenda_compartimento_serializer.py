from rest_framework import serializers
from codex.models.encomenda_compartimento import EncomendaCompartimento


class EncomendaCompartimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncomendaCompartimento
        fields = ["id", "encomenda", "compartimento"]
