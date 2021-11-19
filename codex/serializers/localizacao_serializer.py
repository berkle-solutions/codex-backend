from rest_framework import serializers
from codex.models.localizacao import Localizacao
from django.http import HttpResponse, JsonResponse

class LocalizacaoSerializer(serializers.ModelSerializer):
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
    
    def search(self, validated_data):
        try:
            # todo: https://www.django-rest-framework.org/api-guide/generic-views/#get_querysetself
            localizacao_existe = Localizacao.objects.filter(bloco=validated_data.get('bloco'), andar=validated_data.get('andar')).exists()
            if not localizacao_existe:
                raise Exception('Localização não localizada')
            
            localizacao = Localizacao.objects.get(bloco=validated_data.get('bloco'), andar=validated_data.get('andar'))
            return JsonResponse(localizacao, safe=False)
        except Exception as e:
            raise e
