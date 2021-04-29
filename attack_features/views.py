from django.shortcuts import render
# Create your views here.
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .serializers import AttackfeaturesSerializer
from rest_framework.response import Response
from datetime import datetime
import pytz


class AttackFeatureRecordCreate(APIView):

    serializer_class = AttackfeaturesSerializer
    permission_classes = [AllowAny]

    http_method_names = ['post']

    def post(self, request, *args, **kwargs):

        attack_id = request.data['attack_id']

        start_time_stamp = request.data['start_time_stamp']

        end_time_stamp = request.data['end_time_stamp']

        start_time_stamp = int(start_time_stamp)

        end_time_stamp = int(end_time_stamp)

        start_time_stamp = datetime.fromtimestamp(start_time_stamp).astimezone(pytz.timezone('Europe/Zurich'))
        end_time_stamp = datetime.fromtimestamp(end_time_stamp).astimezone(pytz.timezone('Europe/Zurich'))

        serializer = self.serializer_class(data={'start_time_stamp' : start_time_stamp, 'attack_id' : attack_id, 'end_time_stamp' : end_time_stamp})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(attack_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
