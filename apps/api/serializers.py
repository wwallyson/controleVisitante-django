

from rest_framework import serializers
from morador.models import Morador
from visitantes.models import Visitante
from porteiros.models import Porteiro
from usuarios.models import Usuario

class visitanteSerializer(serializers.ModelSerializer):
    class meta:
        model = Visitante
        fields = '__all__'
        
class porteiroSerializer(serializers.ModelSerializer):
    class meta:
       model = Porteiro
       fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class meta:
       model = Usuario
       fields = '__all__'
       
class UsuarioSerializer(serializers.ModelSerializer):
    class meta:
       model = Morador
       fields = '__all__'
  

       