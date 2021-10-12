from rest_framework import serializers
from codex.models.pessoa import Pessoa
from django.contrib.auth.hashers import make_password

#Serializer
class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = "__all__"
    
    # creates a new pessoa and encrypt password
    def create(self, validated_data):
        print("TO CAINBDO AQUI")
        #TODO: get first perfil intance by id and save this instance
        pessoa = Pessoa.objects.create(**validated_data)
        print(pessoa)
        pessoa.set_password(validated_data["senha"])
        pessoa.save()
                
        return pessoa