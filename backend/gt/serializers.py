from importlib.resources import path
from rest_framework import serializers
from .models import Gt

class GtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gt
        fields = ('id', 'title', 'destination','path')