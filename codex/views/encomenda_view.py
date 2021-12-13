from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view
from rest_framework.response import Response
from codex.models.encomenda import Encomenda
from codex.models.fila_encomenda import FilaEncomenda
from codex.models.encomenda_compartimento import EncomendaCompartimento
from codex.serializers.fila_encomenda_serializer import FilaEncomendaSerializer
from codex.serializers.encomenda_serializer import EncomendaSerializer
from codex.serializers.encomenda_compartimento_serializer import EncomendaCompartimentoSerializer
from codex.enums.fila_status import fila_status_enum
from rest_framework import status

class EncomendaView(APIView):
    """instanciamento de classe"""

    @api_view(['POST'])
    def salvar_encomenda(request):
        """guarda encomenda"""
        try:
            serializer_encomenda = EncomendaSerializer(data=request.data)
            if serializer_encomenda.is_valid():
                encomenda = serializer_encomenda.create_encomenda_estoque(request.data)
                fila_encomenda_serializer = FilaEncomendaSerializer(data=encomenda)
                fila_encomenda_serializer.registra_fila_status(encomenda)

                return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise e

    @api_view(['GET'])
    def retorna_encomenda(request):
        """mostra todas as encomenda"""
        try:
            query = FilaEncomenda.objects.all()
            serializer = FilaEncomendaSerializer(query, many=True)
            return Response(serializer.data)
        except Exception as e:
            raise e

    @api_view(['GET'])
    def detalhe_encomenda(request, pk):
        """mostra detalhes de uma unica encomenda"""
        try:
            fila_encomenda = FilaEncomenda.objects.get(id=pk)
            fila_encomenda_serializer = FilaEncomendaSerializer(fila_encomenda, many=False)
            encomenda_id = fila_encomenda_serializer.data['encomenda']['id']
            
            encomenda = fila_encomenda_serializer.data
            
            if EncomendaCompartimento.objects.filter(encomenda = encomenda_id):
                encomenda_compartimento = EncomendaCompartimento.objects.get(encomenda=encomenda_id)  
                encomenda_compartimento_serializer = EncomendaCompartimentoSerializer(encomenda_compartimento, many=False)
                fila_encomenda_dict = dict(fila_encomenda_serializer.data)
                encomenda_compartimento = dict(encomenda_compartimento_serializer.data["compartimento"])
                encomenda = {**fila_encomenda_dict, 'compartimento': { **encomenda_compartimento }}
                
            return Response(encomenda)
        
        except FilaEncomenda.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            raise e

    @api_view(['PUT'])
    def atualizar_encomenda(request):
        """atualiza status da encomenda"""
        try:
            encomenda = Encomenda.objects.get(id=request.data["id"])
            encomenda.descricao = request.data["descricao"]
            encomenda.save()
            
            serializer = EncomendaSerializer(encomenda, many=False)
            return Response(serializer.data)
        except Exception as e:
            raise e

    @api_view(['DELETE'])
    def deletar_encomenda(request, pk):
        """Deleta encomenda"""
        try:
            if pk:
                encomenda = Encomenda.objects.get(id=pk)
                encomenda.delete()
                return Response(status=204)
            else:
                raise "Por favor, informe o ID da encomenda"
        except Exception as e:
            raise e
        
    @api_view(['POST'])
    def registrar_encomenda_estoque(request):
        """Atualiza encomenda no status fila"""
        try:
            encomenda_compartimento_serializer = EncomendaCompartimentoSerializer(data=request.data)
            if encomenda_compartimento_serializer.is_valid():
                encomenda_compartimento_serializer.create(request.data)
                status_fila_enum = fila_status_enum()

                request.data['status_fila'] = status_fila_enum.EM_ESTOQUE
                
                serializer_fila_encomenda = FilaEncomendaSerializer()
                serializer_fila_encomenda.atualiza_fila_status(request.data)
                
                return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise APIException(e)
        
    @api_view(['POST'])
    def resgatar_encomenda(request):
        """"""
        try:
            encomenda_serializer = EncomendaSerializer(data=request.data)
            encomenda = encomenda_serializer.rescue_encomenda_estoque(request.data)
            
            status_fila_enum = fila_status_enum()
            request.data['status_fila'] = status_fila_enum.RETIRADO
            request.data['encomenda'] = encomenda.id
            
            serializer_fila_encomenda = FilaEncomendaSerializer()
            serializer_fila_encomenda.atualiza_fila_status(request.data)
        
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise e