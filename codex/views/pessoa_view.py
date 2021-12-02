from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.exceptions import APIException
from codex.serializers.pessoa_serializer import PessoaSerializer
from codex.serializers.localizacao_serializer import LocalizacaoSerializer
from codex.models.pessoa import Pessoa
from codex.exceptions.pessoa import pessoa_exception
# services
from codex.services.infobip import (send_user_pin, verify_user_pin, resend_verify_user_pin)

class PessoaView(APIView):
    
    @api_view(['POST'])
    def salvar_pessoa(request):
        try:
            pessoa_serializer = PessoaSerializer(data=request.data)
            if pessoa_serializer.is_valid():
                pessoa_pin_id = pessoa_serializer.create(request.data)

                if request.data.get('localizacao'):
                    localizacao = {}
                    pessoa = Pessoa.objects.get(email=pessoa_serializer.data.get('email'))
                    localizacao['bloco'] = request.data['localizacao']['bloco']
                    localizacao['andar'] = request.data['localizacao']['andar']
                    localizacao['unidade'] = request.data['localizacao']['unidade']
                    localizacao['pessoa'] = pessoa.id

                    localizacao_serializar = LocalizacaoSerializer(data=localizacao)
                    if localizacao_serializar.is_valid():
                        localizacao_serializar.create(localizacao)
                
                
                pin_id = {
                    'pinId': pessoa_pin_id
                }
                
                return JsonResponse(pin_id)
            exceptions = pessoa_exception()
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
            raise APIException(e)
    
    @api_view(['GET'])
    def detalhe_pessoa(request, pk):
        try:
            pessoa = Pessoa.objects.get(id=pk)
            serializer = PessoaSerializer(pessoa, many=False)
            return Response(serializer.data)
        except Exception as e:
            raise APIException(e)
    
    @api_view(['GET'])
    def retorna_pessoas(request):
        try:
            pessoas = Pessoa.objects.all()
            serializer = PessoaSerializer(pessoas, many=True)
            return Response(serializer.data)
        except Exception as e:
            raise APIException(e)
    
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
            raise APIException(e)
        
    @api_view(['POST'])
    def buscar_pessoas_por_andar_bloco(request):
        try:
            localizacao_serializer = LocalizacaoSerializer()
            pessoas_encontradas_serializer = LocalizacaoSerializer(localizacao_serializer.search_persons(request.data), many=True)
            return Response(pessoas_encontradas_serializer.data)
        except Exception as e:
            raise APIException(e)
        
    @api_view(['POST'])
    def enviar_pin_2fa(request):
        try:
            send_user_pin(request.data['celular'])
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise APIException(e)
        
    @api_view(['POST'])
    def verificar_pin_2fa(request):
        try:
            verify_user_pin(request.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise APIException(e)
        
    @api_view(['POST'])
    def reenviar_pin_2fa(request):
        try:
            resend_verify_user_pin(request.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            raise APIException(e)