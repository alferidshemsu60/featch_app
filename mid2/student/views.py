from django.shortcuts import render
from rest_framework import generics
from .serializers import studinfoserializer

from .models import studentinfo

# Create your views here.
class Liststud(generics.ListCreateAPIView):
    serializer_class = studinfoserializer
    queryset = studentinfo.objects.all()

class Delstud(generics.RetrieveDestroyAPIView):
    serializer_class = studinfoserializer
    queryset = studentinfo.objects.all()
