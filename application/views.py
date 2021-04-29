from django.shortcuts import render

# Create your views here.
from .models import Application
from .serializers import ApplicaitonSerializer
from rest_framework import mixins
from rest_framework import generics, status
from organization.models import Organization
from rest_framework.response import Response


class ApplicationList(generics.ListAPIView, generics.CreateAPIView):

    queryset = Application.objects.all()
    serializer_class = ApplicaitonSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        # request_data = request.copy()
        request.POST._mutable = True
        print(request)
        print(type(request.data))

        organization_id = request.data['organization_id']
        print(organization_id)

        try :
            organization = int(organization_id)
            return self.create(request, *args, **kwargs)

        except ValueError:


            organization_name = request.data['organization_id']
            organization_id = ''
            request.data['organization_id'] = organization_id
            request.data['organization_name'] = organization_name
            serializer = self.get_serializer(data=request.data)
            print(serializer.is_valid())
            print(serializer.validated_data)
            print(serializer.errors)
            print(request.data)
            return self.create(request, *args, **kwargs)

