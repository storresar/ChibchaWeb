from rest_framework import routers, urlpatterns
from .views import facturacion_viewset
from django.conf.urls import include,url

router = routers.DefaultRouter()

router.register(r'facturacion', facturacion_viewset,basename='facturacion')

urlpatterns = [
    url(r'^api/(?P<cod_cliente>.+)/$', facturacion_viewset.as_view({'get': 'list'}))
]
urlpatterns = router.urls