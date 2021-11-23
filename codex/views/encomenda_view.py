from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from codex.models.encomenda import Encomenda
from codex.serializers.encomenda_serializer import EncomendaSerializer

class EncomendaView(APIView):
    """instanciamento de classe"""

    @api_view(['POST'])
    def salvar_encomenda(request):
        """guarda encomenda"""
        try:
            serializer_encomenda = EncomendaSerializer(data=request.data)
            if serializer_encomenda.is_valid():
                serializer_encomenda.create(request.data)
                return Response(serializer_encomenda.data)
        except Exception as e:
            raise e

    @api_view(['GET'])
    def retorna_encomenda(request):
        """mostra todas as encomenda"""
        try:
            query = Encomenda.objects.all()
            serializer = EncomendaSerializer(query, many=True)
            return Response(serializer.data)
        except Exception as e:
            raise e

    @api_view(['GET'])
    def detalhe_encomenda(request, pk):
        """mostra detalhes de uma unica encomenda"""
        try:
            query = Encomenda.objects.get(id=pk)
            serializer = EncomendaSerializer(query, many=False)
            return Response(serializer.data)
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
            encomenda_serializer = EncomendaSerializer(data=request.data)
            fila_status = encomenda_serializer.register_encomenda_estoque(request.data)
        except Exception as e:
            raise e