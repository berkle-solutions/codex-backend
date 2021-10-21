from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from codex.models.encomenda import Encomenda
from codex.serializers.encomenda_serializer import EncomendaSerializer
# from rest_framework.renderers import JSONRenderer


class EncomendaView(APIView):
    """instanciamento de classe"""

    @api_view(['POST'])
    def salvar_encomenda(self, request):
        """guarda encomenda"""
        try:
            serializer = EncomendaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            raise e

    @api_view(['GET'])
    def retorna_encomenda(self, request):
        """mostra todas as encomenda"""
        try:
            query = Encomenda.objects.all()
            serializer = EncomendaSerializer(query, many=True)
            return Response(serializer.data)
        except Exception as e:
            raise e

    @api_view(['GET'])
    def detalhe_encomenda(self, request, pk):
        """mostra detalhes de uma unica encomenda"""
        try:
            query = Encomenda.objects.get(id=pk)
            serializer = EncomendaSerializer(query, many=False)
            return Response(serializer.data)
        except Exception as e:
            raise e

    @api_view(['PUT'])
    def atualizar_encomenda(self, request):
        """atualiza status da encomenda"""
        try:
            serializer = EncomendaSerializer(data=request.data)
            if serializer.is_valid():
                encomenda = Encomenda.objects.get(id=request.data["id"])
                encomenda.descricao = request.data["descricao"]
                encomenda.save()
                return Response(serializer.data)
            else:
                raise "Dados invalidos"
        except Exception as e:
            raise e

    @api_view(['DELETE'])
    def deletar_encomenda(self, request, pk):
        try:
            if pk:
                encomenda = Encomenda.objects.get(id=pk)
                encomenda.delete()
                serializers = EncomendaSerializer(encomenda, many=False)
                return Response(serializers.data)
            else:
                raise "Por favor, informe o ID da encomenda"
        except Exception as e:
            raise e
