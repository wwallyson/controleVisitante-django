

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from dashboard.views import index
from morador.views import moradores
from visitantes.views import registrar_visitante, informacoes_visitante, finalizar_visita
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ,name='index'),
    path('moradores/', moradores ,name='moradores'),
     
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'logout.html'), name= 'logout' ),
    
    path('registrar-visitante/', registrar_visitante, name='registrar_visitante'),
    path('visitante/<int:pk>', informacoes_visitante, name='informacoes_visitante'),
    path('visitante/<int:pk>/finalizar-visita', finalizar_visita, name='finalizar_visita'),
    
    path('api/', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]
