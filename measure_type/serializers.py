
from .models import Measuretype
from rest_framework import serializers

class MeasuretypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measuretype
        fields = '__all__'
