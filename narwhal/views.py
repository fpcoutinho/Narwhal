from rest_framework import viewsets, generics, views, filters
from django_filters.rest_framework import DjangoFilterBackend
from narwhal.models import Relatorio, Circuito, Imagem
from narwhal.serializers import *
from narwhal.utils import relatorio_exporta


class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    ordering_fields = ["data", "autor", "local", "temperatura", "clima"]
    search_fields = ["data", "local", "temperatura", "clima"]
    filterset_fields = ["autor", "local"]


class CircuitoViewSet(viewsets.ModelViewSet):
    queryset = Circuito.objects.all()
    serializer_class = CircuitoSerializer


class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer


class ListaImagensPorRelatorio(generics.ListAPIView):
    def get_queryset(self):
        queryset = Imagem.objects.filter(rel_pai__pk=self.kwargs["rel_id"])
        return queryset

    serializer_class = ListaImagensPorRelatorioSerializer


class ListaCircuitosPorRelatorio(generics.ListAPIView):
    def get_queryset(self):
        queryset = Circuito.objects.filter(rel_pai__pk=self.kwargs["rel_id"])
        return queryset

    serializer_class = ListaCircuitosPorRelatorioSerializer


class ExportarRelatorio(views.APIView):
    def post(self, request, rel_id):
        response = relatorio_exporta(request, rel_id)
        print(response)
        return response
