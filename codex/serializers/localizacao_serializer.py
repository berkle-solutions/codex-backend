from rest_framework import serializers
from codex.models.localizacao import Localizacao


class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ['id', 'bloco', 'andar', 'unidade', 'pessoa']
