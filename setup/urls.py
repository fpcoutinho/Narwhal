from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from narwhal.views import (
    RelatorioViewSet,
    CircuitoViewSet,
    ImagemViewSet,
    ListaImagensPorRelatorio,
    ListaCircuitosPorRelatorio,
    ExportarRelatorio,
)
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Narwhal API",
        default_version="v1",
        description="Este projeto é uma API rest automatizadora do processo de geração laudos de engenheiros eletricistas.",
        terms_of_service="https://github.com/fpcoutinho/narwhal",
        contact=openapi.Contact(email="fpcoutinho5@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register("relatorios", RelatorioViewSet, basename="Relatorios")
router.register("circuitos", CircuitoViewSet, basename="Circuitos")
router.register("imagens", ImagemViewSet, basename="Imagens")

urlpatterns = [
    path("access/", admin.site.urls),
    path("auth/", include("auth.urls")),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", RedirectView.as_view(url="docs/")),
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
