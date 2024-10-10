from rest_framework import viewsets
from api.serializers import UsuarioSerializer
from porteiros.models import Porteiro
from usuarios.models import Usuario
from visitantes.models import Visitante

  
class UsuarioViewSet(viewsets.ModelViewSet):
   queryset = Usuario.objects.all()
   serializer_class = UsuarioSerializer

class PorteiroViewSet(viewsets.ModelViewSet):
   queryset = Porteiro.objects.all()
   serializer_class = UsuarioSerializer
   
   
class VisitanteViewSet(viewsets.ModelViewSet):
   queryset = Visitante.objects.all()
   serializer_class = UsuarioSerializer  
   
   
