from rest_framework import serializers
from .models import studentinfo

class studinfoserializer(serializers.ModelSerializer):
    class Meta:
        model = studentinfo
        fields = '__all__'

      