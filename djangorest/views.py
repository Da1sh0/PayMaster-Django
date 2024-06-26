# views.py
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status, viewsets # type: ignore
from .serializer import IndependienteSerializer, CalculosSerializer
from .models import Independiente, Calculos, DatosCalculos
from django.http import Http404 # type: ignore
from django.shortcuts import get_object_or_404 # type: ignore
from .calculos import calcular_salario_base, calcular_ibc, calcular_salud, calcular_pension, calcular_arl, calcular_ccf

class IndependienteViewSet(viewsets.ModelViewSet):
    queryset = Independiente.objects.all()
    serializer_class = IndependienteSerializer

class CalculosViewSet(viewsets.ModelViewSet):
    queryset = Calculos.objects.all()
    serializer_class = CalculosSerializer

class CalculosGenerales(APIView):
    def get(self, request, numero_identificacion, format=None):
        try:
            independiente = get_object_or_404(Independiente, numero_identificacion=numero_identificacion)
            
            # Realizar los cálculos utilizando las funciones importadas
            salario_base = calcular_salario_base(independiente)
            ibc = calcular_ibc(independiente)
            salud = calcular_salud(independiente)
            pension = calcular_pension(independiente)
            arl = calcular_arl(independiente)
            ccf = calcular_ccf(independiente)

            # Crear una instancia de Calculos con los resultados calculados
            calculos = Calculos.objects.create(
                documento=independiente,
                salud=salud,
                pension=pension,
                arl=arl,
                salarioBase=salario_base,
                cajaCompensacion=ccf,
                # Agrega los demás campos según sea necesario
            )

            # Serializar los datos para enviar una respuesta JSON
            serializer = CalculosSerializer(calculos)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Http404:
            return Response({'error': 'No se encontró el objeto Independiente'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
