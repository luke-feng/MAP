from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City
from .models import Country
from .serializers import CitySerializer
from .serializers import CountrySerializer
from rest_framework import mixins, status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class CountryList(generics.ListAPIView):

    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    Permission_classes = [AllowAny]


class CityDetail(APIView):

    def get(self, request, pk,  *args, **kwargs):
        try:
            city = City.objects.get(cityid=pk)
            serializer = CitySerializer(city)
            return Response(serializer.data)
        except City.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CityList(generics.ListAPIView):

    serializer_class = CitySerializer
    queryset = City.objects.all()
    Permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('countryid',)


