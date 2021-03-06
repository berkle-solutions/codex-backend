from rest_framework import serializers
from codex.models.encomenda import Encomenda
from codex.models.encomenda_compartimento import EncomendaCompartimento
from codex.models.pessoa import Pessoa
# helpers
from codex.helpers.makers import criar_codigo_resgate
# enum
from codex.enums.fila_status import fila_status_enum

class EncomendaSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Encomenda
        fields = '__all__'

    def create_encomenda_estoque(self, validated_data):
        try: 
            pessoa = Pessoa.objects.get(id=validated_data["pessoa"])
            validated_data["pessoa"] = pessoa
            
            codigo_resgate = criar_codigo_resgate()
            validated_data["codigo_resgate"] = codigo_resgate
            
            encomenda = Encomenda.objects.create(**validated_data)

            status_fila_enum = fila_status_enum()
            status_fila = {}
            status_fila['encomenda'] = encomenda.id
            status_fila['pessoa'] = pessoa.id
            status_fila['status_fila'] = status_fila_enum.TRIAGEM
            
            return status_fila
        except Exception as e:
            raise e

    def rescue_encomenda_estoque(self, validated_data):
        try:
            encomenda = Encomenda.objects.get(pessoa_id=validated_data['pessoa'], codigo_resgate=validated_data['codigo_resgate'])
            encomenda_compartimento = EncomendaCompartimento.objects.get(encomenda=encomenda.id)
            encomenda_compartimento.delete()
            return encomenda 
        except Encomenda.DoesNotExist as e:
            raise e