from django.contrib import admin
from django.urls import path
from django.urls import include
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
]
