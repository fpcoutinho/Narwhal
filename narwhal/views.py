from rest_framework import viewsets, generics
from narwhal.models import Relatorio, Circuito, Imagens
from narwhal.serializers import RelatorioSerializer, CircuitoSerializer, ImagensSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CircuitoViewSet(viewsets.ModelViewSet):
    queryset = Circuito.objects.all()
    serializer_class = CircuitoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ImagensViewSet(viewsets.ModelViewSet):
    queryset = Imagens.objects.all()
    serializer_class = ImagensSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
