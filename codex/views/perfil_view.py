from rest_framework.views import APIView
from rest_framework.decorators import api_view
# from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from codex.serializers.perfil_serializer import PerfilSerializer
from codex.models.perfil import Perfil
# from django.db import connection


class PerfilView(APIView):

    @api_view(['POST'])
    def salvar_perfil(request):
        try:
            serializer = PerfilSerializer(data=request.data)
            # inner_join = "SELECT * FROM Perfil INNER JOIN Historico ON Perfil.id = Historico.perfil_id WHERE Perfil.id = %s", [request.data["id"]]
            # inner_join = Perfil.objects.select_related('Historico').get(id=pk)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            raise e

    @api_view(['GET'])
    def retorna_perfis(request):
        try:
            query = Perfil.objects.all()
            # query = Perfil.objects.all()
            # query = Perfil.objects.raw('SELECT * FROM codex_perfil')
            serializers = PerfilSerializer(query, many=True)
            return Response(serializers.data)
        except Exception as e:
            raise e

    @api_view(['GET'])
    def detalhe_perfil(request, pk):
        try:
            query = Perfil.objects.get(id=pk)
            serializer = PerfilSerializer(query, many=False)
            return Response(serializer.data)
        except Exception as e:
            raise e

    @api_view(['PUT'])
    def atualizar_perfil(request):
        try:
            serializer = PerfilSerializer(data=request.data)
            if serializer.is_valid():
                perfil = Perfil.objects.get(id=request.data["id"])
                perfil.descricao = request.data["descricao"]
                perfil.save()
                return Response(serializer.data)
            else:
                raise "Dados invalidos"
        except Exception as e:
            raise e

    @api_view(['DELETE'])
    def deletar_perfil(request, pk):
        try:
            if pk:
                perfil = Perfil.objects.get(id=pk)
                perfil.delete()
                serializers = PerfilSerializer(perfil, many=False)
                return Response(serializers.data)
            else:
                raise "Por favor, informe o ID do perfil"
        except Exception as e:
            raise e
