from rest_framework import serializers
from codex.models.pessoa import Pessoa
from codex.models.perfil import Perfil
from django.contrib.auth.hashers import make_password

#Serializer
class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = "__all__"
    
    def create(self, validated_data):
        perfil_instance = Perfil.objects.get(id=validated_data["perfil"])
        validated_data["perfil"] = perfil_instance
        validated_data["senha"] = make_password(validated_data["senha"])
        pessoa = Pessoa.objects.create(**validated_data)
        pessoa.save()
                
        return pessoa