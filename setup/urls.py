from django.contrib import admin
from django.urls import path
from django.urls import include
from narwhal.views import RelatorioViewSet, CircuitoViewSet, ImagensViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('relatorios', RelatorioViewSet, basename='Relatorios')
router.register('circuitos', CircuitoViewSet, basename='Circuitos')
router.register('imagens', ImagensViewSet, basename='Imagens')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
