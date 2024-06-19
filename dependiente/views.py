from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import viewsets
from . serializer import EmpresaSerializer, EmpleadoSerializer, CalculosSerializer, NovedadesSerializer
from . models import Empresa, Empleado, Calculos, Novedades

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset=Empresa.objects.all()
    serializer_class=EmpresaSerializer
    
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset=Empleado.objects.all()
    serializer_class=EmpleadoSerializer

class CalculosViewSet(viewsets.ModelViewSet):
    queryset=Calculos.objects.all()
    serializer_class=CalculosSerializer

class NovedadesViewSet(viewsets.ModelViewSet):
    queryset=Novedades.objects.all()
    serializer_class=NovedadesSerializer
# Create your views here.

# Create your views here.
