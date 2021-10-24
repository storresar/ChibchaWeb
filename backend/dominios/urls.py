from rest_framework import routers, urlpatterns
from .views import dominio_viewSet
from django.conf.urls import include,url

router = routers.DefaultRouter()

router.register(r'dominios', dominio_viewSet,basename='dominios')

urlpatterns = [
    url(r'^api/(?P<cod_facturacion>.+)/$', dominio_viewSet.as_view({'get': 'list'}))
]

urlpatterns = router.urls