from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from codex.serializers.pessoa_serializer import PessoaSerializer
from codex.models.pessoa import Pessoa

class PessoaView(APIView):
    
    @api_view(['POST'])
    def salvar_pessoa(request):
        try:
            serializer = PessoaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.create(request.data)
                return Response(serializer.data)
            else:
                raise "Dados invalidos"
        except Exception as e:
            raise e
    
    @api_view(['PUT'])
    def atualizar_pessoa(request):
        try:
            serializer = PessoaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.update(request.data)
                return Response(status=200)
            raise "Dados invalidos"
        except Exception as e:
            raise e
    
    @api_view(['GET'])
    def detalhe_pessoa(request, pk):
        try:
            pessoa = Pessoa.objects.get(id=pk)
            serializer = PessoaSerializer(pessoa, many=False)
            return Response(serializer.data)
        except Exception as e:
            raise e
    
    # for (admin, sindico, porteiro)
    # body {
    #    tenandId, userRole(perfil),    
    # }
    # RN -> checar se o userId é correspondente ao tenantId e checar se a role é valida
    
    @api_view(['POST'])
    def retorna_pessoas(request):
        return Response(status=200)
    
    @api_view(['DELETE'])
    def deletar_pessoa(request, pk):
        try:
            if pk:
                pessoa = Pessoa.objects.get(id=pk)
                pessoa.delete()
                return Response(status=200)
            else:
               raise "Por favor, informe o ID da pessoa" 
        except Exception as e:
            raise e
    