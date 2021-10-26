from codex.models.pessoa import Pessoa
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import RefreshToken
#from codex.serializers.pessoa_serializer import PessoaSerializer

class AutenticacaoView(APIView):
    
    @api_view(['POST'])
    def autenticar_usuario(request):
        try:
            usuario = Pessoa.objects.get(email=request.data["email"])
            if not usuario:
                return Exception('Usuário não localizado!')
        
            refresh = RefreshToken.for_user(usuario)
            
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        except Exception as e:
            raise e