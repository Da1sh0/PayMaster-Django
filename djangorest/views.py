from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . serializer import IndependienteSerializer, CalculosSerializer, NovedadesSerializer
from . models import Independiente, Calculos, Novedades

class IndependienteViewSet(viewsets.ModelViewSet):
    queryset=Independiente.objects.all()
    serializer_class=IndependienteSerializer

class IndependienteCreate(APIView):
    def post(self, request, format=None):
        serializer = IndependienteViewSet(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CalculosViewSet(viewsets.ModelViewSet):
    queryset=Calculos.objects.all()
    serializer_class=CalculosSerializer
    
class NovedadesViewSet(viewsets.ModelViewSet):
    queryset=Novedades.objects.all()
    serializer_class=NovedadesSerializer
# Create your views here.
