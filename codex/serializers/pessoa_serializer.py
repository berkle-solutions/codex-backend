from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from codex.models.pessoa import Pessoa
from codex.models.perfil import Perfil
from codex.serializers.perfil_serializer import PerfilSerializer
from codex.helpers.makers import criar_random_password
from codex.helpers.email import enviar_email_cadastro
from codex.exceptions.pessoa import pessoa_exception

# services
from codex.services.infobip import (create_new_person, send_user_pin)

class PessoaSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer(many=False, read_only=True)
    class Meta:
        model = Pessoa
        fields = '__all__'
    
    def create(self, validated_data):
        try:
            if Pessoa.objects.filter(email=validated_data["email"]).exists():
                exceptions = pessoa_exception()
                raise Exception(exceptions.EMAIL_ALREADY_IN_USE)

            random_password = criar_random_password()
            perfil_instance = Perfil.objects.get(id=validated_data["perfil"])
            
            validated_data["perfil"] = perfil_instance
            validated_data["senha"] = make_password(random_password)
           
            pessoa = Pessoa.objects.create(**validated_data)
            
            create_new_person({
                "nome": validated_data["nome"],
                "email": validated_data["email"],
                "celular": validated_data["celular"]
            })
            
            enviar_email_cadastro(pessoa.email, random_password)
            
            send_pin = send_user_pin(validated_data["celular"])
            pin_code_id = send_pin['pinId']
             
            return pin_code_id
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