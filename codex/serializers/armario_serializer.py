from rest_framework import serializers
from codex.models.armario import Armario


class ArmarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Armario
        fields = ['id', 'descricao']