from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from codex.serializers.perfil_serializer import PerfilSerializer
from codex.models.perfil import Perfil

class PerfilView(APIView):
    
    @api_view(['POST'])
    @renderer_classes([JSONRenderer]) 
    def guardar_perfil(request):
        query = Perfil.objects.raw('INSERT INTO codex_perfil (descricao) VALUES (%s)', [request.data])
        serializers = PerfilSerializer(query, many=True)
        return Response(serializers.data)