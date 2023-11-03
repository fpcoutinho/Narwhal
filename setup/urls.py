from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from narwhal.views import RelatorioViewSet, CircuitoViewSet, ImagemViewSet, ListaImagensPorRelatorio, ListaCircuitosPorRelatorio
from rest_framework import routers

router = routers.DefaultRouter()
router.register('relatorios', RelatorioViewSet, basename='Relatorios')
router.register('circuitos', CircuitoViewSet, basename='Circuitos')
router.register('imagens', ImagemViewSet, basename='Imagens')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('relatorios/<int:rel_id>/imagens/', ListaImagensPorRelatorio.as_view()),
    path('relatorios/<int:rel_id>/circuitos/', ListaCircuitosPorRelatorio.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
