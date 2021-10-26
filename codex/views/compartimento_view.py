from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from codex.serializers.compartilhamento_serializer import Compartilhamento, CompartilhamentoSerializer
from codex.models.compartilhamento import Compartilhamento
from rest_framework import status


class CompartimentoView(APIView):
    @api_view(['GET'])
    def retorna_compartimentos_por_armario(request, armario_id):
        try:
            compartimentos_por_armario = Compartilhamento.objects.filter(armario_id=armario_id)
            compartimentos_por_armario_serializer = CompartilhamentoSerializer(compartimentos_por_armario, many=True)
            return Response(compartimentos_por_armario_serializer.data)
        except Compartilhamento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            raise ex
    
    
    @api_view(['GET'])
    def detalhe_compartimento(request, pk):
        try:
            compartimento = Compartilhamento.objects.get(pk=pk)
            compartimento_serializer = CompartilhamentoSerializer(compartimento)
            return Response(compartimento_serializer.data)
        except Compartilhamento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            raise ex
    
    @api_view(['POST'])
    def salvar_compartimento(request):
        try:
            compartimento_serializer = CompartilhamentoSerializer(data=request.data)
            if compartimento_serializer.is_valid():
                compartimento_serializer.save()
                return Response(compartimento_serializer.data, status=status.HTTP_201_CREATED)
            return Response(compartimento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise ex
    
    @api_view(['PUT'])
    def atualizar_compartimento(request, pk):
        try:
            compartimento = Compartilhamento.objects.get(pk=pk)
            compartimento_serializer = CompartilhamentoSerializer(compartimento, data=request.data)
            if compartimento_serializer.is_valid():
                compartimento_serializer.save()
                return Response(compartimento_serializer.data)
            return Response(compartimento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Compartilhamento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            raise ex
    
    @api_view(['DELETE'])
    def deletar_compartimento(request, pk):
        try:
            compartimento = Compartilhamento.objects.get(pk=pk)
            compartimento.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Compartilhamento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            raise ex
