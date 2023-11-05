from rest_framework import viewsets, generics, views, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from narwhal.models import Relatorio, Circuito, Imagem
from narwhal.serializers import *
from narwhal.utils import relatorio_exporta


class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
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
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaImagensPorRelatorio(generics.ListAPIView):
    def get_queryset(self):
        queryset = Imagem.objects.filter(rel_pai__pk=self.kwargs["rel_id"])
        return queryset

    serializer_class = ListaImagensPorRelatorioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaCircuitosPorRelatorio(generics.ListAPIView):
    def get_queryset(self):
        queryset = Circuito.objects.filter(rel_pai__pk=self.kwargs["rel_id"])
        return queryset

    serializer_class = ListaCircuitosPorRelatorioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ExportarRelatorio(views.APIView):
    def post(self, request, rel_id):
        response = relatorio_exporta(request, rel_id)
        print(response)
        return response

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
