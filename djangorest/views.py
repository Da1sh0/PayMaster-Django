from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status, viewsets # type: ignore
from . serializer import IndependienteSerializer, CalculosSerializer
from .models import Independiente, Calculos, DatosCalculos
from django.shortcuts import render, get_object_or_404 # type: ignore
from django.http import JsonResponse # type: ignore
from .forms import DatosCalculosForm # type: ignore


class IndependienteViewSet(viewsets.ModelViewSet):
    queryset = Independiente.objects.all()
    serializer_class = IndependienteSerializer


class IndependienteCreate(APIView):
    def post(self, request, format=None):
        serializer = IndependienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CalculosViewSet(viewsets.ModelViewSet):
    queryset = Calculos.objects.all()
    serializer_class = CalculosSerializer


class CalculosGenerales(APIView):
    def post(self, request, numero_identificacion):
        independiente = get_object_or_404(Independiente, pk=numero_identificacion)

        datos_calculos, created = DatosCalculos.objects.get_or_create(documento=independiente)
        form = DatosCalculosForm(request.POST, instance=datos_calculos)
        if form.is_valid():
            calculos = form.save(commit=False)
            if created:
                calculos.documento = independiente
            calculos.save()

        datos_calculos = DatosCalculos.objects.filter(documento=independiente)
        for objeto in datos_calculos:
            salario_base = objeto.salarioBase
            nivel_arl = objeto.arl
            ccf = objeto.CCF
            porcentaje_ibc = objeto.ibc

        ibc = salario_base * (porcentaje_ibc / 100)
        if ibc < 1300000:
            ibc = 1300000

        salud = ibc * 0.125
        pension = ibc * 0.16

        arl = self.calcular_arl(ibc, nivel_arl)

        if ccf == 'Si':
            ccf = ibc * 0.04
        else:
            ccf = 0

        context = {
            'independiente': independiente.numero_identificacion,
            'salario_base': salario_base,
            'ibc': ibc,
            'salud': salud,
            'pension': pension,
            'arl': arl,
            'ccf': ccf,
        }

        return JsonResponse(context)

    @staticmethod
    def calcular_arl(ibc, arl_nivel):
        arl = 0
        if arl_nivel == '1':
            arl = ibc * 0.00522
        elif arl_nivel == '2':
            arl = ibc * 0.01044
        elif arl_nivel == '3':
            arl = ibc * 0.02436
        elif arl_nivel == '4':
            arl = ibc * 0.04350
        elif arl_nivel == '5':
            arl = ibc * 0.06960
        elif arl_nivel == '0':
            arl = 0
        return arl
