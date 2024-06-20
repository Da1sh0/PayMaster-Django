from rest_framework import serializers # type: ignore
from . models import Independiente, Calculos, Novedades

class IndependienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Independiente
        fields = '__all__'

class CalculosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Calculos
        fields = '__all__'
        
class NovedadesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Novedades
        fields = '__all__'