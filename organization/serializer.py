from rest_framework import serializers
from .models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        # fields = [
        #         #     'sectorid',
        #         #     'sector_name',
        #         #     'modify_time',
        #         #     'is_valid',
        #         # ]
        fields = '__all__'
