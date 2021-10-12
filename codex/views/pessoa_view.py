from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from codex.serializers.pessoa_serializer import PessoaSerializer
# from codex.models.pessoa import Pessoa

class PessoaView(APIView):
    
    @api_view(['POST'])
    def salvar_pessoa(request):
        try:
            serializer = PessoaSerializer(data=request.data)
            print(serializer.is_valid())
            # if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.data)
            return Response(status=200)
        except Exception as e:
            raise e
    
    