from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from codex.serializers.compartimento_serializer import (
    Compartimento,
    CompartimentoSerializer,
)
from codex.models.compartimento import Compartimento
from rest_framework import status


class CompartimentoView(APIView):
    @api_view(["GET"])
    def retorna_compartimentos_por_armario(request, armario_id):
        try:
            compartimentos_por_armario = Compartimento.objects.filter(
                armario_id=armario_id
            )
            compartimentos_por_armario_serializer = CompartimentoSerializer(
                compartimentos_por_armario, many=True
            )
            return Response(compartimentos_por_armario_serializer.data)
        except Compartimento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            raise ex

    @api_view(["GET"])
    def detalhe_compartimento(request, pk):
        try:
            compartimento = Compartimento.objects.get(pk=pk)
            compartimento_serializer = CompartimentoSerializer(compartimento)
            return Response(compartimento_serializer.data)
        except Compartimento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            raise ex

    @api_view(["POST"])
    def salvar_compartimento(request):
        try:
            compartimento_serializer = CompartimentoSerializer(data=request.data)
            if compartimento_serializer.is_valid():
                compartimento_serializer.save()
                return Response(
                    compartimento_serializer.data, status=status.HTTP_201_CREATED
                )
            return Response(
                compartimento_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as ex:
            raise ex

    @api_view(["PUT"])
    def atualizar_compartimento(request, pk):
        try:
            compartimento = Compartimento.objects.get(pk=pk)
            compartimento_serializer = CompartimentoSerializer(
                compartimento, data=request.data
            )
            if compartimento_serializer.is_valid():
                compartimento_serializer.save()
                return Response(compartimento_serializer.data)
            return Response(
                compartimento_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        except Compartimento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            raise ex

    @api_view(["DELETE"])
    def deletar_compartimento(request, pk):
        try:
            compartimento = Compartimento.objects.get(pk=pk)
            compartimento.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Compartimento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            raise ex
