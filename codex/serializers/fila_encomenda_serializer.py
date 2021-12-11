from rest_framework import serializers
# models
from codex.models.encomenda import Encomenda
from codex.models.pessoa import Pessoa
from codex.models.fila_encomenda import FilaEncomenda
from codex.models.statusfila import StatusFila
# serializers
from codex.serializers.encomenda_serializer import EncomendaSerializer
from codex.serializers.pessoa_serializer import PessoaSerializer
from codex.serializers.statusfila_serializer import StatusFilaSerializer

class FilaEncomendaSerializer(serializers.ModelSerializer):
    encomenda = EncomendaSerializer(many=False, read_only=True)
    pessoa = PessoaSerializer(many=False, read_only=True)
    status_fila = StatusFilaSerializer(many=False, read_only=True)
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
            return fila_encomenda.save()
        except Exception as e:
            raise e

    def atualiza_fila_status(self, validated_data):
        try:
            encomenda = Encomenda.objects.get(id=validated_data["encomenda"])
            fila_encomenda = FilaEncomenda.objects.get(encomenda_id=encomenda.id, pessoa_id=encomenda.pessoa.id)
            status = StatusFila.objects.get(id=validated_data["status_fila"])
            fila_encomenda.status_fila = status
            
            return fila_encomenda.save()
            
        except Encomenda.DoesNotExist as e:
            raise e
        except FilaEncomenda.DoesNotExist as e:
            raise e
        except StatusFila.DoesNotExist as e:
            raise e
        except Exception as e:
            raise e
        