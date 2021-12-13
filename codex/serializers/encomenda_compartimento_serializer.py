from rest_framework import serializers
from codex.models.pessoa import Pessoa
from codex.models.encomenda import Encomenda
from codex.models.compartimento import Compartimento
from codex.models.encomenda_compartimento import EncomendaCompartimento
from codex.serializers.encomenda_serializer import EncomendaSerializer
from codex.serializers.compartimento_serializer import CompartimentoSerializer
# service
from codex.services.infobip import send_message_whatsapp

class EncomendaCompartimentoSerializer(serializers.ModelSerializer):
    encomenda = EncomendaSerializer(many=False, read_only=True)
    compartimento = CompartimentoSerializer(many=False, read_only=True)
    class Meta:
        model = EncomendaCompartimento
        fields = ['id','encomenda', 'compartimento']
        
    def create(self, validated_data):
        try:
            encomenda = Encomenda.objects.get(id=validated_data.get('encomenda'))
            compartimento = Compartimento.objects.get(id=validated_data.get('compartimento'))
            
            new_dict = {
                "encomenda": encomenda,
                "compartimento": compartimento,
            }
            
            message = 'Seu código de resgate da encomenda ' + encomenda.descricao + ' é ' + encomenda.codigo_resgate
            contato = { "phone": encomenda.pessoa.celular }
            
            send_message_whatsapp(contato, message)

            return EncomendaCompartimento.objects.create(**new_dict)
        except Encomenda.DoesNotExist as e:
            raise e
        except Compartimento.DoesNotExist as e:
            raise e
        except Exception as e:
            raise e
        