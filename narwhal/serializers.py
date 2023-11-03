from rest_framework import serializers
from .models import Relatorio, Circuito, Imagem

class RelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relatorio
        fields = '__all__'

class CircuitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuito
        fields = '__all__'

class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = '__all__'

class ListaImagensPorRelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ['id', 'img']

class ListaCircuitosPorRelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuito
        fields = ['id', 'modelo', 'fase', 'disjuntor', 'descricao', 'condutor', 'corrente']