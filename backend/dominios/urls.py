from rest_framework import routers, urlpatterns
from .views import dominio_viewSet

router = routers.DefaultRouter()

router.register(r'dominios', dominio_viewSet,basename='dominios')

urlpatterns = router.urls