from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CustomAuthToken,empleado_viewset
from django.urls import include
from django.urls import path


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'empleados',empleado_viewset )

urlpatterns = [
    path('token-auth/', CustomAuthToken.as_view()),
]

urlpatterns += router.urls