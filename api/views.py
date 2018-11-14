from django.shortcuts import render
from rest_framework import generics
from App import models
from . import serializers

# Create your views here.

class ListTest(generics.ListCreateAPIView):
    queryset = models.Est.objects.all()
    serializer_class = serializers.TestSerializer

class DetailTest(generics.RetrieveAPIView):
    queryset = models.Est.objects.all()
    serializer_class = serializers.TestSerializer