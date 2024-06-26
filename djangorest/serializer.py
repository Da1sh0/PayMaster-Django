from rest_framework import serializers # type: ignore
from . models import Independiente, Calculos

class IndependienteSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(use_url=True)
    class Meta:
        model = Independiente
        fields = '__all__'

class CalculosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Calculos
        fields = '__all__'
        