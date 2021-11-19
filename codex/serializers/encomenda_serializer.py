from rest_framework import serializers
from codex.models.encomenda import Encomenda
from codex.models.pessoa import Pessoa
from codex.helpers.makers import criarCodigoResgate
# serializer
from codex.serializers.fila_encomenda_serializer import FilaEncomendaSerializer
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
            
            codigo_resgate = criarCodigoResgate()
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
        