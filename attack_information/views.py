import json
from collections import Counter
from datetime import datetime
import datetime as dt

import pytz
from django.db import connection
from django.db.models import Count, Sum, Q, F, Avg
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from attack_features.models import Attackfeatures
from attack_features.serializers import AttackfeaturesSerializer
from .serializers import AttackinformationDeserializer, IncidentCataSerializer, MonthlyLossSumSerializer, \
    MonthlyAttackTimesSerializer, AttackTimesBySectorSerializer, AttackTypeLossSumSerializer, \
    MonthlyImpactRatingSerializer, YearlyIncidentEffectTimesSerializer, MonthlySecurityCompromiseSerializer, \
    YearlyTopAttackerInfrastructureSerializer, YearlyTopThreatActorTypeSerializer, YearlyTopAttackerToolSerializer, \
    YearlyTopMalwareTypeSerializer, YearlyTopSystemTypeSerializer, AttackinformationSerializer, YearlyLossDurationSerializer, \
    YearlyTopLossPropertySerializer, YearlyTopAssetTypeSerializer, MonthlyLossDurationSerializer, MonthlyIncidentCataSerializer, \
    YearlyLossSumBySectorSerializer, YearlyDiscoveryMethodSerializer, YearlyLossSumByLossCateSerializer

from information_sharing.models import Assettype, Systemtype, Malwaretype, Attackertool, Threatactortype, Incidenteffect,\
    Lossproperty, Attackerinfrastructure, Discoverymethod, Impactrating, Lossduration
from .models import Attackinformation


class IncidentCateList(APIView):

    serializer_class = IncidentCataSerializer
    queryset = Attackinformation.objects.all()
    Permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            year = dt.date.today().year - 1


            if group == "sector":

                queryset = Attackinformation.objects.values('incident_category__incident_category') \
                            .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id)) \
                            .annotate(total=Count('attack_id'))

            elif group == "org":

                queryset = Attackinformation.objects.values('incident_category__incident_category') \
                            .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id)) \
                            .annotate(total=Count('attack_id'))

            serializer = IncidentCataSerializer(queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class MonthlyIncidentCateList(APIView):

    serializer_class = MonthlyIncidentCataSerializer
    queryset = Attackinformation.objects.all()
    Permission_classes = [AllowAny]
    http_method_names = ['get']

    def get(self, request, group, orgid, *args, **kwargs):

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)


        try:

            year = dt.date.today().year - 1


            if group == "sector":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__month',
                                                            'incident_category__incident_category') \
                            .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=orgid)) \
                            .annotate(total=Count('attack_id'))

            elif group == "org":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__month',
                                                            'incident_category__incident_category') \
                            .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=orgid)) \
                            .annotate(total=Count('attack_id'))

            serializer =  MonthlyIncidentCataSerializer(queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class MonthlyLossSum(APIView):

    serializer_class = MonthlyLossSumSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1
        end = dt.date.today()
        start = dt.date(dt.date.today().year - 1,
                        dt.date.today().month, dt.date.today().day)

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":
                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__month') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id)) \
                    .annotate(total_loss=Sum(F('corporate_income_loss') + F('organization_productive_loss')
                                             + F('sla_loss') + F('indirect_loss') + F('costofequipmentreplacement')
                                             + F('costofrepair')))
            elif group == "org":
                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__month') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id)) \
                    .annotate(total_loss=Sum(F('corporate_income_loss') + F('organization_productive_loss')
                                             + F('sla_loss') + F('indirect_loss') + F('costofequipmentreplacement')
                                             + F('costofrepair')))



            serializer = MonthlyLossSumSerializer(queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyLossSumByLossCate(APIView):

    serializer_class = YearlyLossSumByLossCateSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1
        end = dt.date.today()
        start = dt.date(dt.date.today().year - 1,
                        dt.date.today().month, dt.date.today().day)

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":
                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id)) \
                    .annotate(total_col=Sum(F('corporate_income_loss')),
                              total_opl = Sum(F('organization_productive_loss')),
                              total_sla = Sum(F('sla_loss')),
                              total_il = Sum(F('indirect_loss')),
                              total_coer = Sum(F('costofequipmentreplacement')),
                              total_cor = Sum(F('costofrepair')))

            elif group == "org":
                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id)) \
                    .annotate(total_col=Sum(F('corporate_income_loss')),
                              total_opl=Sum(F('organization_productive_loss')),
                              total_sla=Sum(F('sla_loss')),
                              total_il=Sum(F('indirect_loss')),
                              total_coer=Sum(F('costofequipmentreplacement')),
                              total_cor=Sum(F('costofrepair')))



            serializer = YearlyLossSumByLossCateSerializer(queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyLossSumBySector(APIView):

    serializer_class = YearlyLossSumBySectorSerializer
    queryset = Attackinformation.objects.all()

    Permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, *args, **kwargs):

        try:


            year = dt.date.today().year - 1


            queryset = Attackinformation.objects.values('sector_id__sector_name') \
                        .filter(Q(attack_id__start_time_stamp__year=year)) \
                        .annotate(total_loss=Sum(F('corporate_income_loss') + F('organization_productive_loss')
                                             + F('sla_loss') + F('indirect_loss') + F('costofequipmentreplacement')
                                             + F('costofrepair')))



            serializer = YearlyLossSumBySectorSerializer(queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class MonthlyAttackTimes(APIView):
    serializer_class = MonthlyAttackTimesSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, orgid, *args, **kwargs):

        year = dt.date.today().year - 1

        try:
            queryset = Attackinformation.objects.values('attack_id__start_time_stamp__month') \
                .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=orgid)) \
                .annotate(total_attacktimes=Count('attack_id'))

            serializer = MonthlyAttackTimesSerializer(queryset, many=True)
            
            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class AttackTimesBySector(APIView):
    serializer_class = AttackTimesBySectorSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, *args, **kwargs):

        year = dt.date.today().year - 1

        try:
            queryset = Attackinformation.objects.values('sector_id__sector_name') \
                .filter(Q(attack_id__start_time_stamp__year=year)) \
                .annotate(total_attacktimes=Count('attack_id'))

            serializer = AttackTimesBySectorSerializer(queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class AttackTypeLossSum(APIView):

    serializer_class = AttackTypeLossSumSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":
                queryset = Attackinformation.objects.values('incident_category__incident_category') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id)) \
                    .annotate(total_loss=Sum(F('corporate_income_loss') + F('organization_productive_loss')
                                             + F('sla_loss') + F('indirect_loss') + F('costofequipmentreplacement')
                                             + F('costofrepair')))

            elif group == "org":
                queryset = Attackinformation.objects.values('incident_category__incident_category') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id)) \
                    .annotate(total_loss=Sum(F('corporate_income_loss') + F('organization_productive_loss')
                                             + F('sla_loss') + F('indirect_loss') + F('costofequipmentreplacement')
                                             + F('costofrepair')))

            serializer = AttackTypeLossSumSerializer(queryset, many=True)

            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class MonthlyImpactRating(APIView):

    serializer_class = MonthlyImpactRatingSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            impact_rating_dict = {}
            impact_rating_key = []
            impact_rating = Impactrating.objects.values('impact_rating')
            for ir in impact_rating:
                key = ir['impact_rating']
                impact_rating_key.append(key)
                impact_rating_dict[key] = [0]*12

            if group == "sector":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__month',
                                                            'impact_rating__impact_rating') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id)) \
                    .annotate(total=Count('attack_id'))
            elif group == "org":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__month',
                                                            'impact_rating__impact_rating') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id)) \
                    .annotate(total=Count('attack_id'))

            for i in queryset:
                month = i['attack_id__start_time_stamp__month']
                for key in impact_rating_key:
                    if key in i.values():
                        impact_rating_dict[key][month-1] = i['total']

            impact_rating_dict['labels'] = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

            serializer = MonthlyImpactRatingSerializer(queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyIncidentEffectTimes(APIView):

    serializer_class = YearlyIncidentEffectTimesSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('incident_effect__incident_effect') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id), ~Q(incident_effect=None)) \
                    .annotate(total=Count('attack_id'))

            elif group == "org":

                queryset = Attackinformation.objects.values('incident_effect__incident_effect') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id), ~Q(incident_effect=None)) \
                    .annotate(total=Count('attack_id'))

            serializer = YearlyIncidentEffectTimesSerializer(queryset, many=True)
            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class MonthlySecurityCompromise(APIView):

    serializer_class = MonthlySecurityCompromiseSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__month',
                                                            'security_compromise__security_compromise') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id)) \
                    .annotate(total=Count('attack_id'))

            elif group == "org":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__month',
                                                            'security_compromise__security_compromise') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id)) \
                    .annotate(total=Count('attack_id'))

            serializer = MonthlySecurityCompromiseSerializer(queryset, many=True)

            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyTopAttackerInfrastructure(APIView):

    serializer_class = YearlyTopAttackerInfrastructureSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'attacker_infrastructure__attacker_infrastructure') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id), ~Q(attacker_infrastructure=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            elif group == "org":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'attacker_infrastructure__attacker_infrastructure') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id), ~Q(attacker_infrastructure=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            serializer = YearlyTopAttackerInfrastructureSerializer(queryset, many=True)

            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class YearlyTopThreatActorType(APIView):

    serializer_class = YearlyTopThreatActorTypeSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'threat_actor_type__threat_actor_type') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id), ~Q(threat_actor_type=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            elif group == "org":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'threat_actor_type__threat_actor_type') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id), ~Q(threat_actor_type=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            serializer = YearlyTopThreatActorTypeSerializer(queryset, many=True)

            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyTopAttackerTool(APIView):

    serializer_class = YearlyTopAttackerToolSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'attacker_tool__attacker_tool') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id), ~Q(attacker_tool=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            elif group == "org":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'attacker_tool__attacker_tool') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id), ~Q(attacker_tool=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            serializer = YearlyTopAttackerToolSerializer(queryset, many=True)

            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyTopMalwareType(APIView):

    serializer_class = YearlyTopMalwareTypeSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'malware_type__malware_type') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id), ~Q(malware_type=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            elif group == "org":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'malware_type__malware_type') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id), ~Q(malware_type=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            serializer = YearlyTopMalwareTypeSerializer(queryset, many=True)
            
            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyTopSystemType(APIView):

    serializer_class = YearlyTopSystemTypeSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'system_type__system_type') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id), ~Q(system_type=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            elif group == "org":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'system_type__system_type') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id), ~Q(system_type=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            serializer = YearlyTopSystemTypeSerializer(queryset, many=True)

            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyTopAssetType(APIView):

    serializer_class = YearlyTopAssetTypeSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'asset_type__asset_type') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id), ~Q(asset_type=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            elif group == "org":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'asset_type__asset_type') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id), ~Q(asset_type=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            serializer = YearlyTopAssetTypeSerializer(queryset, many=True)

            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class YearlyTopLossProperty(APIView):

    serializer_class = YearlyTopLossPropertySerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'loss_property__loss_property') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id), ~Q(loss_property=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            elif group == "org":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'loss_property__loss_property') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id), ~Q(loss_property=None)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            serializer = YearlyTopLossPropertySerializer(queryset, many=True)

            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyLossDuration(APIView):

    serializer_class = YearlyLossDurationSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'loss_duration__loss_duration')\
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id))\
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')


            elif group == "org":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year',
                                                            'incident_category__incident_category',
                                                            'loss_duration__loss_duration') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            serializer = YearlyLossDurationSerializer(queryset, many=True)

            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class MonthlyLossDuration(APIView):

    serializer_class = MonthlyLossDurationSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__month',
                                                            'incident_category__incident_category',
                                                            'loss_duration__loss_duration')\
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')


            elif group == "org":

                queryset = Attackinformation.objects.values('attack_id__start_time_stamp__month',
                                                            'incident_category__incident_category',
                                                            'loss_duration__loss_duration') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=1)) \
                    .annotate(total=Count('attack_id')) \
                    .order_by('-total')

            serializer = MonthlyLossDurationSerializer(queryset, many=True)

            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyDiscoveryMethod(APIView):
    serializer_class = YearlyDiscoveryMethodSerializer
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            if group == "sector":
                queryset = Attackinformation.objects.values('discovery_method__discovery_method') \
                    .filter(Q(attack_id__start_time_stamp__year=year)) \
                    .annotate(total=Count('attack_id'))

            elif group == "org":
                queryset = Attackinformation.objects.values('discovery_method__discovery_method') \
                    .filter(Q(attack_id__start_time_stamp__year=year)) \
                    .annotate(total=Count('attack_id'))

            serializer = YearlyDiscoveryMethodSerializer(queryset, many=True)

            return Response(serializer.data)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyTopIpWatchlist(APIView):
    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1
        ip_watchlist_all = []

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('ip_watchlist') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id))

            elif group == "org":

                queryset = Attackinformation.objects.values('ip_watchlist') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id))



            for i in queryset:
                if i['ip_watchlist'] is not None and i['ip_watchlist'] != '':
                    ip_watchlist = i['ip_watchlist'].split(';')
                    ip_watchlist_all = ip_watchlist_all + ip_watchlist


            ip_watchlist_all = Counter(ip_watchlist_all)
            ip_watchlist = sorted(ip_watchlist_all.items(), key=lambda x: x[1], reverse=True)[:5]
            ip_watchlist_list = [x[0] for x in ip_watchlist]
            ip_watchlist_times = [x[1] for x in ip_watchlist]

            ip_watchlist_json = {'group': group, 'id': id, 'watchlist': ip_watchlist_list, 'times': ip_watchlist_times}

            return Response(ip_watchlist_json)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyTopMaliciousEmailWatchlist(APIView):

    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1
        malicious_e_mail_all = []

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)


        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('malicious_e_mail') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id))

            elif group == "org":

                queryset = Attackinformation.objects.values('malicious_e_mail') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id))


            for i in queryset:
                if i['malicious_e_mail'] is not None and i['malicious_e_mail'] != '':
                    malicious_e_mail = i['malicious_e_mail'].split(';')
                    malicious_e_mail_all = malicious_e_mail_all + malicious_e_mail


            malicious_e_mail_all = Counter(malicious_e_mail_all)
            malicious_e_mail = sorted(malicious_e_mail_all.items(), key=lambda x: x[1], reverse=True)[:5]
            malicious_e_mail_list = [x[0] for x in malicious_e_mail]
            malicious_e_mail_times = [x[1] for x in malicious_e_mail]

            malicious_e_mail_json = {'group': group, 'id': id, 'watchlist': malicious_e_mail_list, 'times': malicious_e_mail_times}

            return Response(malicious_e_mail_json)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyTopFileHashWatchlist(APIView):

    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1
        file_hash_watchlist_all = []

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)


        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('file_hash_watchlist') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id))

            elif group == "org":

                queryset = Attackinformation.objects.values('file_hash_watchlist') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id))


            for i in queryset:
                if i['file_hash_watchlist'] is not None and i['file_hash_watchlist'] != '':
                    file_hash_watchlist = i['file_hash_watchlist'].split(';')
                    file_hash_watchlist_all = file_hash_watchlist_all + file_hash_watchlist

            file_hash_watchlist_all = Counter(file_hash_watchlist_all)
            file_hash_watchlist = sorted(file_hash_watchlist_all.items(), key=lambda x: x[1], reverse=True)[:5]
            file_hash_watchlist_list = [x[0] for x in file_hash_watchlist]
            file_hash_watchlist_times = [x[1] for x in file_hash_watchlist]

            file_hash_watchlist_json = {'group': group, 'id': id, 'watchlist': file_hash_watchlist_list, 'times': file_hash_watchlist_times}

            return Response(file_hash_watchlist_json)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyTopDomainWatchlist(APIView):

    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1
        domain_watchlist_all = []

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('domain_watchlist') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id))

            elif group == "org":

                queryset = Attackinformation.objects.values('domain_watchlist') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id))


            for i in queryset:
                if i['domain_watchlist'] is not None and i['domain_watchlist'] != '':
                    domain_watchlist = i['domain_watchlist'].split(';')
                    domain_watchlist_all = domain_watchlist_all + domain_watchlist

            domain_watchlist_all = Counter(domain_watchlist_all)
            domain_watchlist = sorted(domain_watchlist_all.items(), key=lambda x: x[1], reverse=True)[:5]
            domain_watchlist_list = [x[0] for x in domain_watchlist]
            domain_watchlist_times = [x[1] for x in domain_watchlist]

            domain_watchlist_json = {'group': group, 'id': id, 'watchlist': domain_watchlist_list, 'times': domain_watchlist_times}

            return Response(domain_watchlist_json)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class YearlyTopURLWatchlist(APIView):

    queryset = Attackinformation.objects.all()
    permission_classes = [AllowAny]

    http_method_names = ['get']

    def get(self, request, group, id, *args, **kwargs):

        year = dt.date.today().year - 1
        url_watchlist_all = []

        if group not in ['sector', 'org']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:

            if group == "sector":

                queryset = Attackinformation.objects.values('url_watchlist') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(sector_id=id))

            elif group == "org":

                queryset = Attackinformation.objects.values('url_watchlist') \
                    .filter(Q(attack_id__start_time_stamp__year=year), Q(organization_id=id))


            for i in queryset:
                if i['url_watchlist'] is not None and i['url_watchlist'] != '':
                    url_watchlist = i['url_watchlist'].split(';')
                    url_watchlist_all = url_watchlist_all + url_watchlist


            url_watchlist_all = Counter(url_watchlist_all)
            url_watchlist = sorted(url_watchlist_all.items(), key=lambda x: x[1], reverse=True)[:5]
            url_watchlist_list = [x[0] for x in url_watchlist]
            url_watchlist_times = [x[1] for x in url_watchlist]

            url_watchlist_json = {'group': group, 'id': id, 'watchlist': url_watchlist_list, 'times': url_watchlist_times}

            return Response(url_watchlist_json)

        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class AttackInformationRecordCreate(APIView):

    serializer_class = AttackinformationDeserializer
    permission_classes = [AllowAny]

    http_method_names = ['post']

    def post(self, request, *args, **kwargs):

        request_data = request.POST.copy()  #querydict

        attack_id = request.POST.get('attack_id')   #json

        user_id = request.POST.get('user_id')

        organization_id = request.POST.get('organization_id')

        sector_id = request.POST.get('sector_id')

        costofequipmentreplacement = request.POST.get('costofequipmentreplacement')

        costofrepair = request.POST.get('costofrepair')

        corporate_income_loss = request.POST.get('corporate_income_loss')

        organization_productive_loss = request.POST.get('organization_productive_loss')

        sla_loss = request.POST.get('sla_loss')

        indirect_loss = request.POST.get('indirect_loss')

        impact_rating = request.POST.get('impact_rating')

        incident_category = request.POST.get('incident_category')

        security_compromise = request.POST.get('security_compromise')

        loss_duration = request.POST.get('loss_duration')

        malicious_e_mail = request.POST.get('malicious_e_mail')

        ip_watchlist = request.POST.get('ip_watchlist')

        file_hash_watchlist = request.POST.get('file_hash_watchlist')

        domain_watchlist = request.POST.get('domain_watchlist')

        url_watchlist = request.POST.get('url_watchlist')


        l1 = int(costofrepair) + int(corporate_income_loss) + int(organization_productive_loss)

        l2 = int(corporate_income_loss) + int(organization_productive_loss)

        l3 = int(costofequipmentreplacement) + int(sla_loss) + int(indirect_loss)

        try :
            af = Attackfeatures.objects.get(pk=attack_id)
        except Attackfeatures.DoesNotExist:
            start_time_stamp = request.POST.get('start_time_stamp')

            end_time_stamp = request.POST.get('end_time_stamp')


            start_time_stamp = int(start_time_stamp)

            end_time_stamp = int(end_time_stamp)

            start_time_stamp = datetime.fromtimestamp(start_time_stamp).astimezone(pytz.timezone('Europe/Zurich'))
            end_time_stamp = datetime.fromtimestamp(end_time_stamp).astimezone(pytz.timezone('Europe/Zurich'))

            serializer_attack = AttackfeaturesSerializer(
                data={'start_time_stamp': start_time_stamp, 'attack_id': attack_id, 'end_time_stamp': end_time_stamp})

            if serializer_attack.is_valid(raise_exception=True):
                serializer_attack.save()

        if 'incidentEffect' in request_data:
            incident_effect = request_data.pop('incidentEffect')[0]

            incident_effect = incident_effect.split(";")

        else:
            incident_effect = []
        if 'lossProperty' in request_data:
                loss_property = request_data.pop('lossProperty')[0]

                loss_property = loss_property.split(";")
        else:
                loss_property = []
        if 'attackerInfrastructure' in request_data:
                attacker_infrastructure = request_data.pop('attackerInfrastructure')[0]

                attacker_infrastructure = attacker_infrastructure.split(";")
        else:
                attacker_infrastructure = []
        if 'threatActorType' in request_data:
                threat_actor_type = request_data.pop('threatActorType')[0]

                threat_actor_type = threat_actor_type.split(";")
        else:
                threat_actor_type = []
        if 'attackerTool' in request_data:
                attacker_tool = request_data.pop('attackerTool')[0]

                attacker_tool = attacker_tool.split(";")
        else:
                attacker_tool = []

        if 'malwareType' in request_data:
                malware_type = request_data.pop('malwareType')[0]

                malware_type = malware_type.split(";")
                print(malware_type)
        else:
                malware_type = []

        if 'systemType' in request_data:
                system_type = request_data.pop('systemType')[0]

                system_type = system_type.split(";")

        else:
                system_type = []

        if 'assetType' in request_data:
                asset_type = request_data.pop('assetType')[0]

                asset_type = asset_type.split(";")
                print(type(asset_type))
        else:
                asset_type = []

        if 'discoveryMethod' in request_data:
                discovery_method = request_data.pop('discoveryMethod')[0]

                discovery_method = discovery_method.split(";")
        else:
                discovery_method = []

        serializer = self.serializer_class(data={
                                                 'attack_id': attack_id, 'user_id': user_id, 'organization_id': organization_id,
                                                 'sector_id': sector_id, 'costofequipmentreplacement': costofequipmentreplacement,
                                                 'costofrepair': costofrepair, 'corporate_income_loss': corporate_income_loss,
                                                 'organization_productive_loss': organization_productive_loss,
                                                 'sla_loss': sla_loss, 'indirect_loss': indirect_loss,
                                                 'impact_rating': impact_rating, 'incident_category': incident_category,
                                                 'security_compromise': security_compromise, 'loss_duration': loss_duration,
                                                 'malicious_e_mail': malicious_e_mail, 'ip_watchlist': ip_watchlist,
                                                 'file_hash_watchlist': file_hash_watchlist, 'domain_watchlist': domain_watchlist,
                                                 'url_watchlist': url_watchlist,
                                                 'l1': l1, 'l2': l2, 'l3': l3
                                                })

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            AI = Attackinformation.objects.get(pk=attack_id)
            for i in incident_effect:
                if i != "":
                    ie = Incidenteffect.objects.get(pk=i)
                    AI.incident_effect.add(ie)
            for i in loss_property:
                if i != "":
                    lp = Lossproperty.objects.get(pk=i)
                    AI.loss_property.add(lp)
            for i in attacker_infrastructure:
                if i != "":
                    ai = Attackerinfrastructure.objects.get(pk=i)
                    AI.attacker_infrastructure.add(ai)
            for i in threat_actor_type:
                if i != "":
                    tat = Threatactortype.objects.get(pk=i)
                    AI.threat_actor_type.add(tat)
            for i in attacker_tool:
                if i != "":
                    at = Attackertool.objects.get(pk=i)
                    AI.attacker_tool.add(at)
            for i in malware_type:
                if i != "":
                    mt = Malwaretype.objects.get(pk=i)
                    AI.malware_type.add(mt)
            for i in system_type:
                if i != "":
                    st = Systemtype.objects.get(pk=i)
                    AI.system_type.add(st)
            for i in asset_type:
                if i != "":
                    aty = Assettype.objects.get(pk=i)
                    AI.asset_type.add(aty)
            for i in discovery_method:
                if i != "":
                    dm = Discoverymethod.objects.get(pk=i)
                    AI.discovery_method.add(dm)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttackInformationDetail(generics.GenericAPIView):

    serializer_class = AttackinformationSerializer
    Permission_classes = [AllowAny]

    def get(self, request, pk,  *args, **kwargs):
        try:
            AI = Attackinformation.objects.get(attack_id=pk)
            serializer = AttackinformationSerializer(AI)
            return Response(serializer.data)
        except AI.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

