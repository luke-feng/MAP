from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Organization
from organization.serializer import OrganizationSerializer


class OrganizationList(generics.ListAPIView):

    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    Permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('sector','is_valid',)
