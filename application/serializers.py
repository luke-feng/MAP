from rest_framework import serializers
from .models import Application

class ApplicaitonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
