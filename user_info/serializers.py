from rest_framework import serializers
from .models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    sector_name = serializers.CharField(source='sectorid.sector_name', read_only=True)
    organization_name = serializers.CharField(source='organizationid.organization_name', read_only=True)
    country_name = serializers.CharField(source='country.countryname', read_only=True)
    city_name = serializers.CharField(source='city.cityname', read_only=True)
    class Meta:
        model = UserInfo
        fields = [
                    'userid',
                    'userfirstname',
                    'userlastname',
                    'useremail',
                    'userscale',
                    'sectorid',
                    'sector_name',
                    'organizationid',
                    'organization_name',
                    'country',
                    'country_name',
                    'city',
                    'city_name',
                    'postal_code',
                    'address',
                ]

class UserInfoPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
