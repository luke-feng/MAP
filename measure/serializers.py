from .models import Measures
from rest_framework import serializers

class MeasuresSerializer(serializers.ModelSerializer):
    measure_type_name = serializers.CharField(source='measure_type_id.measure_name', read_only=True)
    incident_category_name = serializers.CharField(source='incident_category.incident_category', read_only=True)
    class Meta:
        model = Measures
        fields = '__all__'
