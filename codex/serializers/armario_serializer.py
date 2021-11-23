from rest_framework import serializers
from codex.models.armario import Armario
from codex.serializers.compartimento_serializer import CompartimentoSerializer


class ArmarioSerializer(serializers.ModelSerializer):
    compartimentos = CompartimentoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Armario
        fields = ['id', 'descricao', 'compartimentos']