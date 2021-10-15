from rest_framework import routers, urlpatterns
from rest_framework import viewsets
from .views import ticket_viewset

router = routers.DefaultRouter()

router.register(r'ticket', ticket_viewset,basename='ticket')

urlpatterns = router.urls