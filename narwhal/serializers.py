from rest_framework import serializers
from .models import Relatorio, Circuito, Imagens

class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        fields = '__all__'

class CircuitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuito
        fields = '__all__'

class ImagensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagens
        fields = '__all__'
