from rest_framework import serializers

from .models import Attackfeatures


class AttackfeaturesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attackfeatures
        fields = '__all__'
