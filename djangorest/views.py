from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import viewsets
from . serializer import IndependienteSerializer, CalculosSerializer, NovedadesSerializer
from . models import Independiente, Calculos, Novedades

class IndependienteViewSet(viewsets.ModelViewSet):
    queryset=Independiente.objects.all()
    serializer_class=IndependienteSerializer


class CalculosViewSet(viewsets.ModelViewSet):
    queryset=Calculos.objects.all()
    serializer_class=CalculosSerializer
    
class NovedadesViewSet(viewsets.ModelViewSet):
    queryset=Novedades.objects.all()
    serializer_class=NovedadesSerializer
# Create your views here.
