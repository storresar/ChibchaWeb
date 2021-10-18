from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CustomAuthToken,empleado_viewset,cliente_viewset
from django.urls import include
from django.conf.urls import url
from django.urls import path


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'empleados',empleado_viewset )
router.register(r'clientes',cliente_viewset)

urlpatterns = [
    path('token-auth/', CustomAuthToken.as_view()),
    url(r'^api/(?P<cod_usuario>.+)/$', UsuarioViewSet.as_view({'get': 'list'}))
]

urlpatterns += router.urls