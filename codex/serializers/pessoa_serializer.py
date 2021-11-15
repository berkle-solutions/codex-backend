from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from codex.models.pessoa import Pessoa
from codex.models.perfil import Perfil
from codex.helpers.makers import criarRandomPassword
from codex.helpers.email import enviarEmailDeCadastro
from codex.exceptions.pessoa import pessoaExceptions

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
    
    def create(self, validated_data):
        try:
            if Pessoa.objects.filter(email=validated_data["email"]).exists():
                exceptions = pessoaExceptions()
                raise Exception(exceptions.EMAIL_ALREADY_IN_USE)

            random_password = criarRandomPassword()
            perfil_instance = Perfil.objects.get(id=validated_data["perfil"])
            
            validated_data["perfil"] = perfil_instance
            validated_data["senha"] = make_password(random_password)
           
            pessoa = Pessoa.objects.create(**validated_data)
            pessoa.save()
            
            enviarEmailDeCadastro(pessoa.email, random_password) 
             
            return pessoa
        except Exception as e:
            raise e
            
    
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
