from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from codex.serializers.pessoa_serializer import PessoaSerializer
from codex.models.pessoa import Pessoa
from codex.exceptions.pessoa import pessoaExceptions

class PessoaView(APIView):
    
    @api_view(['POST'])
    def salvar_pessoa(request):
        try:
            serializer = PessoaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.create(request.data)
                return Response(status=status.HTTP_204_NO_CONTENT)
            exceptions = pessoaExceptions()
            raise Exception(exceptions.INVALID_FIELDS)
        except Exception as e:
            raise APIException(e)
    
    @api_view(['PUT'])
    def atualizar_pessoa(request):
        try:
            serializer = PessoaSerializer(data=request.data)
            serializer.update(request.data)
            return Response(status=200)
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
    
    @api_view(['GET'])
    def retorna_pessoas(request):
        try:
            pessoas = Pessoa.objects.all()
            serializer = PessoaSerializer(pessoas, many=True)
            return Response(serializer.data)
        except Exception as e:
            raise e
    
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
    