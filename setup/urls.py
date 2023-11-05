from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from narwhal.views import (
    RelatorioViewSet,
    CircuitoViewSet,
    ImagemViewSet,
    ListaImagensPorRelatorio,
    ListaCircuitosPorRelatorio,
    ExportarRelatorio,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("relatorios", RelatorioViewSet, basename="Relatorios")
router.register("circuitos", CircuitoViewSet, basename="Circuitos")
router.register("imagens", ImagemViewSet, basename="Imagens")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
    path("api/relatorios/<int:rel_id>/imagens/", ListaImagensPorRelatorio.as_view()),
    path(
        "api/relatorios/<int:rel_id>/circuitos/", ListaCircuitosPorRelatorio.as_view()
    ),
    path(
        "api/relatorios/<int:rel_id>/exportar/",
        ExportarRelatorio.as_view(),
        name="exportar_relatorio",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
