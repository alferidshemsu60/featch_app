from rest_framework import serializers
from .models import Teacherinfo

class teachserializer(serializers.ModelSerializer):
    class Meta:
        model = Teacherinfo
        fields = '__all__'