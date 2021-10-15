from rest_framework import serializers
from .models import ticket

class ticket_serializer(serializers.ModelSerializer):
    class Meta:
        model = ticket
        fields = '__all__'