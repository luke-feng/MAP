from rest_framework import serializers
from .models import Attackinformation, Attackinformation2Assettype
from information_sharing.serializers import AssettypeSerializer


class AttackinformationDeserializer(serializers.ModelSerializer):

    class Meta:
        model = Attackinformation
        fields = [
                    'attack_id',
                    'user_id',
                    'organization_id',
                    'sector_id',
                    'costofequipmentreplacement',
                    'costofrepair',
                    'corporate_income_loss',
                    'organization_productive_loss',
                    'sla_loss',
                    'indirect_loss',
                    'impact_rating',
                    'incident_category',
                    'security_compromise',
                    'loss_duration',
                    'malicious_e_mail',
                    'ip_watchlist',
                    'file_hash_watchlist',
                    'domain_watchlist',
                    'url_watchlist',
                    'l1', 'l2', 'l3'

                ]


class AttackinformationSerializer(serializers.ModelSerializer):
    asset_type = serializers.SerializerMethodField()

    class Meta:
        model = Attackinformation
        fields = '__all__'
        depth = 1

    def get_asset_type(self, obj):
        qset = Attackinformation2Assettype.objects.filter(attack_information_id=obj)
        return [Attackinformation2AssettypeSerializer(m).data for m in qset]

class Attackinformation2AssettypeSerializer(serializers.ModelSerializer):
    assettype_name = serializers.ReadOnlyField(source='asset_type.asset_type')
    class Meta:
        model = Attackinformation2Assettype
        fields = ('attack_information_id', 'asset_type_id', 'assettype_name', )


class IncidentCataSerializer(serializers.Serializer):
    incident_category__incident_category = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class MonthlyIncidentCataSerializer(serializers.Serializer):
    attack_id__start_time_stamp__month = serializers.ReadOnlyField()
    incident_category__incident_category = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class MonthlyLossSumSerializer(serializers.Serializer):
    attack_id__start_time_stamp__month = serializers.ReadOnlyField()
    total_loss = serializers.ReadOnlyField()

class YearlyLossSumByLossCateSerializer(serializers.Serializer):
    attack_id__start_time_stamp__year = serializers.ReadOnlyField()
    total_col = serializers.ReadOnlyField()
    total_opl = serializers.ReadOnlyField()
    total_sla = serializers.ReadOnlyField()
    total_il = serializers.ReadOnlyField()
    total_coer = serializers.ReadOnlyField()
    total_cor = serializers.ReadOnlyField()
    total_loss = serializers.ReadOnlyField()

class YearlyLossSumBySectorSerializer(serializers.Serializer):
    sector_id__sector_name = serializers.ReadOnlyField()
    total_loss = serializers.ReadOnlyField()

class MonthlyAttackTimesSerializer(serializers.Serializer):
    attack_id__start_time_stamp__month = serializers.ReadOnlyField()
    total_attacktimes = serializers.ReadOnlyField()

class AttackTimesBySectorSerializer(serializers.Serializer):
    sector_id__sector_name = serializers.ReadOnlyField()

    total_attacktimes = serializers.ReadOnlyField()

class AttackTypeLossSumSerializer(serializers.Serializer):
    incident_category__incident_category = serializers.ReadOnlyField()
    total_loss = serializers.ReadOnlyField()

class MonthlyImpactRatingSerializer(serializers.Serializer):
    attack_id__start_time_stamp__month = serializers.ReadOnlyField()
    impact_rating__impact_rating = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class YearlyIncidentEffectTimesSerializer(serializers.Serializer):
    # attack_id__start_time_stamp__month = serializers.ReadOnlyField()
    incident_effect__incident_effect = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class MonthlySecurityCompromiseSerializer(serializers.Serializer):
    attack_id__start_time_stamp__month = serializers.ReadOnlyField()
    security_compromise__security_compromise = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class YearlyTopAttackerInfrastructureSerializer(serializers.Serializer):
    attack_id__start_time_stamp__year = serializers.ReadOnlyField()
    attacker_infrastructure__attacker_infrastructure = serializers.ReadOnlyField()
    incident_category__incident_category = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class YearlyTopThreatActorTypeSerializer(serializers.Serializer):
    attack_id__start_time_stamp__year = serializers.ReadOnlyField()
    threat_actor_type__threat_actor_type = serializers.ReadOnlyField()
    incident_category__incident_category = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class YearlyTopAttackerToolSerializer(serializers.Serializer):
    attack_id__start_time_stamp__year = serializers.ReadOnlyField()
    attacker_tool__attacker_tool = serializers.ReadOnlyField()
    incident_category__incident_category = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class YearlyTopMalwareTypeSerializer(serializers.Serializer):
    attack_id__start_time_stamp__year = serializers.ReadOnlyField()
    malware_type__malware_type = serializers.ReadOnlyField()
    incident_category__incident_category = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class YearlyTopSystemTypeSerializer(serializers.Serializer):
    attack_id__start_time_stamp__year = serializers.ReadOnlyField()
    system_type__system_type = serializers.ReadOnlyField()
    incident_category__incident_category = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class YearlyTopLossPropertySerializer(serializers.Serializer):
    attack_id__start_time_stamp__year = serializers.ReadOnlyField()
    loss_property__loss_property = serializers.ReadOnlyField()
    incident_category__incident_category = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class YearlyLossDurationSerializer(serializers.Serializer):
    attack_id__start_time_stamp__year = serializers.ReadOnlyField()
    incident_category__incident_category = serializers.ReadOnlyField()
    loss_duration__loss_duration = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class YearlyTopAssetTypeSerializer(serializers.Serializer):
    attack_id__start_time_stamp__year = serializers.ReadOnlyField()
    incident_category__incident_category = serializers.ReadOnlyField()
    asset_type__asset_type = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class MonthlyLossDurationSerializer(serializers.Serializer):
    attack_id__start_time_stamp__month = serializers.ReadOnlyField()
    incident_category__incident_category = serializers.ReadOnlyField()
    loss_duration__loss_duration = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

class YearlyDiscoveryMethodSerializer(serializers.Serializer):
    discovery_method__discovery_method = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()
