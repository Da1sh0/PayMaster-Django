from rest_framework import serializers
from . models import Empresa, Empleado, Calculos, Novedades

class EmpresaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Empresa
        fields = '__all__'
class EmpleadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Empleado
        fields = '__all__'

class CalculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculos
        fields = '__all__'

class NovedadesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Novedades
        fields = '__all__'


