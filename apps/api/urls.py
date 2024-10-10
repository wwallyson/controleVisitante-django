
from django.db import router
from django.urls import include, path
from rest_framework import routers

from api.viewsets import UsuarioViewSet, PorteiroViewSet, VisitanteViewSet

router = routers.DefaultRouter()

router.register(r'usuarios', UsuarioViewSet)
router.register(r'porteiro', PorteiroViewSet)
router.register(r'visitante', VisitanteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


