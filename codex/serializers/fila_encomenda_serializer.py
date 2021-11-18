from rest_framework import serializers
from codex.models.encomenda import Encomenda
from codex.models.pessoa import Pessoa
from codex.models.fila_encomenda import FilaEncomenda
from codex.models.statusfila import StatusFila

class FilaEncomendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilaEncomenda
        fields = '__all__'

    def registra_fila_status(self, validated_data):
        try:
            
            encomenda = Encomenda.objects.get(id=validated_data["encomenda"])
            pessoa = Pessoa.objects.get(id=validated_data["pessoa"])
            status = StatusFila.objects.get(id=validated_data["status_fila"])
            
            validated_data["encomenda"] = encomenda
            validated_data["pessoa"] = pessoa
            validated_data["status_fila"] = status
            
            fila_encomenda = FilaEncomenda.objects.create(**validated_data)
            fila_encomenda.save()
        except Exception as e:
            raise e
