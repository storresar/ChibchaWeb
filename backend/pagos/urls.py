from rest_framework import routers, urlpatterns
from .views import facturacion_viewset

router = routers.DefaultRouter()

router.register(r'facturacion', facturacion_viewset,basename='facturacion')

urlpatterns = router.urls