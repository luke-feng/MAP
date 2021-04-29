from rest_framework import serializers

from information_sharing.models import Assettype, Attackerinfrastructure, Attackertool, Impactrating, Incidentcategory, \
    Incidenteffect, Lossproperty, Malwaretype, Securitycompromise, Systemtype, Threatactortype, Discoverymethod, \
    Lossduration


class AssettypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assettype
        fields = '__all__'

class AttackerinfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attackerinfrastructure
        fields = '__all__'

class AttackertoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attackertool
        fields = '__all__'

class ImpactratingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impactrating
        fields = '__all__'

class IncidentcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidentcategory
        fields = '__all__'

class IncidenteffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidenteffect
        fields = '__all__'

class LosspropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lossproperty
        fields = '__all__'

class MalwaretypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Malwaretype
        fields = '__all__'

class SecuritycompromiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Securitycompromise
        fields = '__all__'

class SystemtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Systemtype
        fields = '__all__'

class ThreatactortypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threatactortype
        fields = '__all__'

class DiscoverymethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discoverymethod
        fields = '__all__'

class LossdurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lossduration
        fields = '__all__'
