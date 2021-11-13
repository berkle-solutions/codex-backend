from rest_framework import serializers
from codex.models.encomenda_compartilhamento import EncomendaCompartilhamento


class EncomendaCompartilhamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncomendaCompartilhamento
        fields = ['id', 'encomenda', 'compartilhamento']