
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework import generics

from .models import Assettype, Attackerinfrastructure, Attackertool, Impactrating, Incidentcategory, Incidenteffect, \
    Lossproperty, Malwaretype, Securitycompromise, Systemtype, Threatactortype, Discoverymethod, Lossduration
from .serializers import AssettypeSerializer, AttackerinfrastructureSerializer, AttackertoolSerializer, \
    ImpactratingSerializer, IncidentcategorySerializer, IncidenteffectSerializer, LosspropertySerializer, \
    MalwaretypeSerializer, SecuritycompromiseSerializer, SystemtypeSerializer, \
    ThreatactortypeSerializer, DiscoverymethodSerializer, LossdurationSerializer


# Create your views here.

class AssettypeList(generics.ListAPIView):

    serializer_class = AssettypeSerializer
    queryset = Assettype.objects.all()
    Permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_valid',)

class AttackerinfrastructureList( generics.ListAPIView):

    serializer_class = AttackerinfrastructureSerializer
    queryset = Attackerinfrastructure.objects.all()
    Permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_valid',)

class AttackertoolList(generics.ListAPIView):

    serializer_class = AttackertoolSerializer
    queryset = Attackertool.objects.all()
    Permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_valid',)

class ImpactratingList(generics.ListAPIView):

    serializer_class = ImpactratingSerializer
    queryset = Impactrating.objects.all()
    Permission_classes = [AllowAny]

class IncidentcategoryList(generics.ListAPIView):

    serializer_class = IncidentcategorySerializer
    queryset = Incidentcategory.objects.all()
    Permission_classes = [AllowAny]

class IncidenteffectList(generics.ListAPIView):

    serializer_class = IncidenteffectSerializer
    queryset = Incidenteffect.objects.all()
    Permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_valid',)

class LosspropertyList(generics.ListAPIView):

    serializer_class = LosspropertySerializer
    queryset = Lossproperty.objects.all()
    Permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_valid',)

class MalwaretypeList(generics.ListAPIView):

    serializer_class = MalwaretypeSerializer
    queryset = Malwaretype.objects.all()
    Permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_valid',)

class SecuritycompromiseList(generics.ListAPIView):

    serializer_class = SecuritycompromiseSerializer
    queryset = Securitycompromise.objects.all()
    Permission_classes = [AllowAny]

class SystemtypeList(generics.ListAPIView):

    serializer_class = SystemtypeSerializer
    queryset = Systemtype.objects.all()
    Permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_valid',)

class ThreatactortypeList(generics.ListAPIView):

    serializer_class = ThreatactortypeSerializer
    queryset = Threatactortype.objects.all()
    Permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_valid',)

class DiscoverymethodList(generics.ListAPIView):

    serializer_class = DiscoverymethodSerializer
    queryset = Discoverymethod.objects.all()
    Permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_valid',)

class LossdurationList(generics.ListAPIView):

    serializer_class = LossdurationSerializer
    queryset = Lossduration.objects.all()
    Permission_classes = [AllowAny]
