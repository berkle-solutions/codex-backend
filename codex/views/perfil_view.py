from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from codex.serializers.perfil_serializer import PerfilSerializer
from codex.models.perfil import Perfil
from django.db import connection

class PerfilView(APIView):
    
    @api_view(['POST'])
    def salvar_perfil(request):
        try:
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO codex_perfil(descricao) VALUES(%s)', [request.data["descricao"]])
                return Response(status=200)
        except Exception as e:
            raise e