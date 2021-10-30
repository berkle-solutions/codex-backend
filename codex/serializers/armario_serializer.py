from rest_framework import serializers
from codex.models.armario import Armario
from codex.serializers.compartilhamento_serializer import CompartilhamentoSerializer


class ArmarioSerializer(serializers.ModelSerializer):
    compartimentos = CompartilhamentoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Armario
        fields = ['id', 'descricao', 'compartimentos']