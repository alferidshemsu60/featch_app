from rest_framework import generics
from .serializers import empinfoserializer

from .models import empinfo

# Create your views here.
class Listemp(generics.ListCreateAPIView):
    serializer_class = empinfoserializer
    queryset = empinfo.objects.all()

class Delemp(generics.RetrieveDestroyAPIView):
    serializer_class = empinfoserializer
    queryset = empinfo.objects.all()
