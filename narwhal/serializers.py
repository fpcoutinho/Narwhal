from rest_framework import serializers
from .models import Relatorio, Circuito, Imagem

class CircuitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuito
        fields = ['modelo', 'fase', 'disjuntor', 'descricao', 'condutor', 'corrente']

class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = '__all__'

class RelatorioSerializer(serializers.ModelSerializer):
    imagens = ImagemSerializer(many=True, read_only=True)
    imagens_do_relatorio = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )
    circuitos = CircuitoSerializer(many=True, read_only=True)
    circuitos_do_relatorio = serializers.ListField(
        child=CircuitoSerializer(),
        write_only=True,
        required=False
    )
    class Meta:
        model = Relatorio
        fields = '__all__'
    
    def create(self, validated_data):
        imagens_data = []
        circuitos_data = []
        if 'imagens_do_relatorio' in validated_data:
            imagens_data = validated_data.pop('imagens_do_relatorio')
        if 'circuitos_do_relatorio' in validated_data:
            circuitos_data = validated_data.pop('circuitos_do_relatorio')
            print("Circuitos data: ")

        relatorio = Relatorio.objects.create(**validated_data)

        for imagem_data in imagens_data:
            Imagem.objects.create(rel_pai=relatorio, img=imagem_data)
        for circuito_data in circuitos_data:
            Circuito.objects.create(rel_pai=relatorio, **circuito_data)

        return relatorio

class ListaImagensPorRelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = ['id', 'img']

class ListaCircuitosPorRelatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circuito
        fields = ['id', 'modelo', 'fase', 'disjuntor', 'descricao', 'condutor', 'corrente']