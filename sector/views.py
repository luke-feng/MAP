from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Sector
from .serializers import SectorSerializer
from rest_framework import mixins, status
from rest_framework import generics

# Create your views here.

@require_http_methods(["POST"])
def add_sector(request):
    print(request.POST)
    response = {}
    try:
        sector = Sector(sector_name=request.POST.get('sector_name'), is_valid=request.POST.get('is_valid'))
        sector.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_sectors(request):
    response = {}
    try:
        sectors = Sector.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", sectors))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@api_view(http_method_names=["GET"])
def show_sector(request):
    sector_list = Sector.objects.all()
    serializer = SectorSerializer(sector_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class SectorListAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):

    serializer_class = SectorSerializer
    queryset = Sector.objects.all()
    Permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        response = {}
        try:
            queryset = Sector.objects.all()
            ser = SectorSerializer(instance=queryset, many=True)
            response['list'] = ser.data
            response['msg'] = 'success'
            response['error_num'] = 0
        except Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1
        return Response(response)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        response = {}

        try:
            sector = Sector(sector_name=request.POST.get('sector_name'), is_valid=request.POST.get('is_valid'))
            sector.save()
            response['msg'] = 'success'
            response['error_num'] = 0
        except Exception as e:
            response['msg'] = str(e)
            response['error_num'] = 1

        return Response(response)


class SectorList(generics.ListAPIView):

    serializer_class = SectorSerializer
    queryset = Sector.objects.all()
    Permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_valid',)


class SectorDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):

    serializer_class = SectorSerializer
    queryset = Sector.objects.all()
    Permission_classes = [AllowAny]

    def get(self, request, pk,  *args, **kwargs):
        try:
            sector = Sector.objects.get(sectorid=pk)
            serializer = SectorSerializer(sector)
            return Response(serializer.data)
        except Sector.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def delete(self, request, pk, *args, **kwargs):
        try:
            sector = Sector.objects.get(sectorid=pk)
            sector.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Sector.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, *args, **kwargs):
        sector = Sector.objects.get(sectorid=pk)
        serializer = SectorSerializer(sector, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

























