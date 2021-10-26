from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from codex.serializers.armario_serializer import ArmarioSerializer
from codex.models.armario import Armario
from rest_framework import status


class ArmarioView(APIView):

    @api_view(['GET'])
    def retorna_armarios(request):
        try:
            armarios = Armario.objects.all()
            armarios_serializer = ArmarioSerializer(armarios, many=True)
            return Response(armarios_serializer.data)
        except Exception as ex:
            raise ex
    
    
    @api_view(['GET'])
    def detalhe_armario(request, pk):
        try:
            armario = Armario.objects.get(pk=pk)
            armario_serializer = ArmarioSerializer(armario)
            return Response(armario_serializer.data)
        except Armario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            raise ex
    
    @api_view(['POST'])
    def salvar_armario(request):
        try:
            armario_serializer = ArmarioSerializer(data=request.data)
            if armario_serializer.is_valid():
                armario_serializer.save()
                return Response(armario_serializer.data, status=status.HTTP_201_CREATED)
            return Response(armario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise ex
    
    @api_view(['PUT'])
    def atualizar_armario(request, pk):
        try:
            armario = Armario.objects.get(pk=pk)
            armario_serializer = ArmarioSerializer(armario, data=request.data)
            if armario_serializer.is_valid():
                armario_serializer.save()
                return Response(armario_serializer.data)
            return Response(armario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Armario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            raise ex
    
    @api_view(['DELETE'])
    def deletar_armario(request, pk):
        try:
            armario = Armario.objects.get(pk=pk)
            armario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Armario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            raise ex
    
        

            

