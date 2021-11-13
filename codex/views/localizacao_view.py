from rest_framework import serializers
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from codex.models.localizacao import Localizacao
from codex.serializers.localizacao_serializer import LocalizacaoSerializer


class LocalizacaoView(APIView):
    """Instanciamento de Classe"""

    @api_view(['GET'])
    def buscar_localizacao(self, request, pk):
        """busca localização"""
        try:
            query = Localizacao.objects.get(id=pk)
            serializer = LocalizacaoSerializer(query, many=False)
            return Response(serializer.data)
        except Exception as e:
            raise e
    
    @api_view(['POST'])
    def salvar_localizacao(self, request):
        """salva localização"""
        try:
             serializer = LocalizacaoSerializer(data=request.data)
             if serializer.is_valid():
                serializer.save()
             return Response(serializer.data)
        except Exception as e:
            raise e

    @api_view(['PUT'])
    def atualizar_localizacao(self, request):
        """atualiza localização"""
        try:
            serializer = LocalizacaoSerializer(data=request.data)
            if serializer.is_valid():
                localizacao = Localizacao.objects.get(id=request.data["id"])
                localizacao.descricao = request.data["descricao"]
                localizacao.save()
                return Response(serializer.data)
            else:
                raise "Dados invalidos"
        except Exception as e:
            raise e