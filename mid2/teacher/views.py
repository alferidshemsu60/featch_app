from rest_framework import generics
from .serializers import teachserializer

from .models import Teacherinfo

# Create your views here.
class Listtech(generics.ListCreateAPIView):
    serializer_class = teachserializer
    queryset = Teacherinfo.objects.all()

class Deltech(generics.RetrieveDestroyAPIView):
    serializer_class = teachserializer
    queryset = Teacherinfo.objects.all()
