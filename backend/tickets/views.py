from rest_framework import viewsets
from .models import ticket
from .serializers import ticket_serializer

class ticket_viewset(viewsets.ModelViewSet):
    queryset = ticket.objects.all()
    serializer_class = ticket_serializer
