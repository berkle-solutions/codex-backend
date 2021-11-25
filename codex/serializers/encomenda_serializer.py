from rest_framework import serializers
from codex.models.encomenda import Encomenda
from codex.models.pessoa import Pessoa
from codex.helpers.makers import criar_codigo_resgate
# serializer
from codex.serializers.fila_encomenda_serializer import FilaEncomendaSerializer
from codex.serializers.pessoa_serializer import PessoaSerializer
# enum
from codex.enums.fila_status import fila_status_enum

class EncomendaSerializer(serializers.ModelSerializer): 
    pessoa = PessoaSerializer(many=False, read_only=True)
    
    class Meta:
        model = Encomenda
        fields = '__all__'

    def create(self, validated_data):
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
            
            serializer_fila_encomenda = FilaEncomendaSerializer(data=status_fila)
            serializer_fila_encomenda.registra_fila_status(status_fila)
            
            return encomenda
        except Exception as e:
            raise e
        
    def register_encomenda_estoque(self, validated_data):
        try:
            
            status_fila_enum = fila_status_enum()
            validated_data['status_fila'] = status_fila_enum.EM_ESTOQUE
            
            serializer_fila_encomenda = FilaEncomendaSerializer()
            return serializer_fila_encomenda.atualiza_fila_status(validated_data)
        except Exception as e:
            raise e