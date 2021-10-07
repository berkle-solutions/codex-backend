from rest_framework import serializers
from codex.models.pessoa import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = [
            'id',
            'nome',
            'email',
            'senha',
            'cpf',
            'data_nascimento',
            'telefone',
            'celular',
            'ativo',
            'perfil'
        ]