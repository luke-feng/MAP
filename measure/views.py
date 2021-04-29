from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from measure.models import Measures
from .serializers import MeasuresSerializer
import datetime as dt
from attack_information.models import Attackinformation
from django.db.models import Count, Sum, Q, F, Avg


class MeasureRecordCreate(generics.CreateAPIView):

    serializer_class = MeasuresSerializer
    permission_classes = [AllowAny]

    http_method_names = ['post']

    def post(self, request, *args, **kwargs):

        vulnerability_without_measure = request.data['vulnerability_without_measure']
        reduced_vulnerability = request.data['reduced_vulnerability']
        reduced_l1_rate = request.data['reduced_l1_rate']
        reduced_l2_rate = request.data['reduced_l2_rate']
        incident_category = request.data['incident_category']
        initial_cost = request.data['initial_cost']
        annual_upgrade = request.data['annual_upgrade']
        annual_maintenance = request.data['annual_maintenance']
        time_period = request.data['time_period']
        discount_rate = request.data['discount_rate']
        organization_id = request.data['organization_id']
        # insurance_amount = request.data['insurance_amount']

        total_cost = float(initial_cost) + float(annual_upgrade) + float(annual_maintenance)

        last_year = dt.date.today().year - 1

        queryset = Attackinformation.objects.values('attack_id__start_time_stamp__year') \
            .filter(Q(attack_id__start_time_stamp__year=last_year), Q(organization_id=organization_id),
                    Q(incident_category=incident_category)) \
            .annotate(total_l1=Sum(F('l1')), total_l2=Sum(F('l2')), total_l3=Sum(F('l3')))

        l1 = 0
        l2 = 0
        l3 = 0
        RC = 0
        R0 = 0
        NPV = 0
        ROSI = 0



        if queryset :

            if queryset[0]['total_l1'] is not None:

                l1 = float(queryset[0]['total_l1'])

            if queryset[0]['total_l2'] is not None:
                l2 = float(queryset[0]['total_l2'])

            if queryset[0]['total_l3'] is not None:
                l3 = float(queryset[0]['total_l3'])

            RC = (float(vulnerability_without_measure) * float(reduced_vulnerability) * (l1 * float(reduced_l1_rate) + l2 * float(reduced_l2_rate) + l3))
            R0 = l1+l2+l3

            ROSI = (R0 - RC - total_cost) / total_cost

            time_period = int(time_period)

            for i in range(1, time_period+1):

                NPV = NPV + ((R0 - RC - float(annual_upgrade) - float(annual_maintenance)) / (1 + float(discount_rate))**i)
                # NPV = NPV - 1

            NPV = NPV - float(initial_cost)


        serializer = MeasuresSerializer(data={'user_id': request.data['user_id'],
                                              'organization_id': request.data['organization_id'],
                                              'measure_type_id': request.data['measure_type_id'],
                                              'measure_description': request.data['measure_description'],
                                              'rosi': ROSI, 'npv': NPV, 'time_period': time_period,
                                              'initial_cost': initial_cost, 'annual_upgrade': annual_upgrade,
                                              'annual_maintenance': annual_maintenance, 'total_cost': total_cost,
                                              'reduced_vulnerability': reduced_vulnerability,
                                              'incident_category': request.data['incident_category'],
                                              'vulnerability_without_measure': vulnerability_without_measure,
                                              'reduced_l1_rate': reduced_l1_rate, 'reduced_l2_rate': reduced_l2_rate,
                                              'discount_rate': discount_rate})
        # print(connection.queries)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeasureRecordList(APIView):
    serializer_class = MeasuresSerializer
    permission_classes = [AllowAny]

    http_method_names = ['get']
    queryset = Measures.objects.all()

    def get(self, request, userid, incident_category, *args, **kwargs):
        try:
            queryset = Measures.objects.filter(Q(incident_category=incident_category), Q(user_id=userid)) \
                            .order_by('-rosi')
            serializer = MeasuresSerializer(queryset, many=True)
            return Response(serializer.data)
        except Measures.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MeasureRecordListByUser(APIView):
    serializer_class = MeasuresSerializer
    permission_classes = [AllowAny]

    http_method_names = ['get']
    queryset = Measures.objects.all()

    def get(self, request, userid, *args, **kwargs):
        try:
            queryset = Measures.objects.filter(Q(user_id=userid))
            serializer = MeasuresSerializer(queryset, many=True)
            return Response(serializer.data)
        except Measures.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# class MeasureRecordListByUserAndIncident (APIView):
#
#     serializer_class = MeasuresSerializer
#     permission_classes = [AllowAny]
#
#     http_method_names = ['get']
#     queryset = Measures.objects.all()
#
#     def get(self, request, userid, *args, **kwargs):
#         try:
#             queryset = Measures.objects.values('incident_category__incident_category') \
#                        .filter(Q(user_id='x2')) \
#                        .annotate(total=Count('measure_id'))
#             serializer = MeasuresSerializer(queryset, many=True)
#             return Response(serializer.data)
#         except Measures.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)










