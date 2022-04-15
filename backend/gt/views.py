from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GtSerializer
from .models import Gt

# Create your views here.

class GtView(viewsets.ModelViewSet):
    serializer_class = GtSerializer
    queryset = Gt.objects.all()