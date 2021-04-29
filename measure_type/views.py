from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework import generics
from measure_type.models import Measuretype
from measure_type.serializers import MeasuretypeSerializer


class MeasuretypeList(generics.ListAPIView):

    serializer_class = MeasuretypeSerializer
    queryset = Measuretype.objects.all()
    Permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_valid',)



