from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet
from django.urls import path, include


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
]

urlpatterns += router.urls