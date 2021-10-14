from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from codex.models import perfil
from codex.models.pessoa import Pessoa
from codex.models.perfil import Perfil
from django.contrib.auth.hashers import make_password

#Serializer
class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = "__all__"
        # fields = []
    
    def create(self, validated_data):
        perfil_instance = Perfil.objects.get(id=validated_data["perfil"])
        validated_data["perfil"] = perfil_instance
        validated_data["senha"] = make_password(validated_data["senha"])
        pessoa = Pessoa.objects.create(**validated_data)
        pessoa.save()
                
        return pessoa
    
    def update(self, validated_data):
        try:
            if validated_data.get("perfil"):
                perfil_instance = Perfil.objects.get(id=validated_data["perfil"])
                validated_data["perfil"] = perfil_instance
                
            if validated_data.get("senha"):
                validated_data["senha"] = make_password(validated_data["senha"])
                
            return Pessoa.objects.filter(id=validated_data["id"]).update(**validated_data)
        except Exception as e:
            raise e
       