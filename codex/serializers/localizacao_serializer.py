from rest_framework import serializers
from codex.models.localizacao import Localizacao
from codex.models.pessoa import Pessoa
from codex.serializers.pessoa_serializer import PessoaSerializer

class LocalizacaoSerializer(serializers.ModelSerializer):
    pessoa = PessoaSerializer(many=False, read_only=True)
    class Meta:
        model = Localizacao
        fields = '__all__'

    def create(self, validated_data):
        try:
            pessoa = Pessoa.objects.get(id=validated_data["pessoa"])
            validated_data["pessoa"] = pessoa
            Localizacao.objects.create(**validated_data)
            
            return True
        except Exception as e:
            raise e
    
    def search_persons(self, validated_data):
        try:
            return Localizacao.objects.filter(bloco=validated_data['bloco'], andar=validated_data['andar'])
        except Exception as e:
            raise e
