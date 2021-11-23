from rest_framework import serializers
from codex.models.encomenda import Encomenda
from codex.models.compartimento import Compartimento
from codex.models.pessoa import Pessoa
from codex.helpers.makers import criar_codigo_resgate
# serializer
from codex.serializers.fila_encomenda_serializer import FilaEncomendaSerializer
from codex.serializers.encomenda_compartimento_serializer import EncomendaCompartimentoSerializer
from codex.serializers.pessoa_serializer import PessoaSerializer

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

            status_fila = {}
            status_fila['encomenda'] = encomenda.id
            status_fila['pessoa'] = pessoa.id
            status_fila['status_fila'] = 1 # triagem
            
            serializer_fila_encomenda = FilaEncomendaSerializer()
            serializer_fila_encomenda.registra_fila_status(status_fila)
            
            return encomenda
        except Exception as e:
            raise e
        
    def register_encomenda_estoque(self, validated_data):
        try:
            encomenda = Encomenda.objects.get(id=validated_data['encomenda'])
            compartimento = Compartimento.objects.get(id=validated_data['compartimento'])
            
            validated_data['encomenda'] = encomenda
            validated_data['compartimento'] = compartimento
            
            encomenda_compartimento_serializer = EncomendaCompartimentoSerializer(data=validated_data)
            encomenda_compartimento_serializer.save()
        except Exception as e:
            raise e