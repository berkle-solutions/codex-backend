from rest_framework import serializers
from codex.models.localizacao import Localizacao
from codex.models.pessoa import Pessoa


class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ['id', 'bloco', 'andar', 'unidade', 'pessoa']

    def create(self, validated_data):
        try:
            pessoa = Pessoa.objects.get(id=validated_data["pessoa"])
            validated_data["pessoa"] = pessoa
            Localizacao.objects.create(**validated_data)
            
            return True
        except Exception as e:
            raise e
        
