from rest_framework import serializers
from .models import empinfo

class empinfoserializer(serializers.ModelSerializer):
    class Meta:
        model = empinfo
        fields = '__all__'