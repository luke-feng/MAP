import django.utils.timezone as timezone

from django.core.exceptions import ValidationError
from django.db import models
import geonamescache
from smart_selects.db_fields import ChainedForeignKey
from django import forms
# from django.forms.fields import DEFAULT_DATE_INPUT_FORMATS
from django.contrib.admin.widgets import AdminDateWidget
from city_country.models import City, Country
from sector.models import Sector

# Create your models here.

# def get_cities_name():
#     gc = geonamescache.GeonamesCache()
#     cities = gc.get_cities()
#     cities_name = []
#
#     for key, value in cities.items():
#         for key2, val2 in value.items():
#             if key2 == 'name':
#                 cities_name.append((key, val2))
#     cities_name = tuple(cities_name)
#     return cities_name
#
# def get_countries_name():
#     gc = geonamescache.GeonamesCache()
#     countries = gc.get_countries()
#
#     countries_name = []
#
#     for key, value in countries.items():
#         for key2, val2 in value.items():
#             if key2 == 'name':
#                 countries_name.append((key, val2))
#     countries_name = tuple(countries_name)
#     return countries_name

# def select_citics(countrycode):
#     gc = geonamescache.GeonamesCache()
#     cities = gc.get_cities()
#     selected_cities = []
#
#     for key, value in cities.items():
#         if value.get('countrycode') == countrycode:
#             city = value.get('name')
#             selected_cities.append((countrycode,city))
#     return selected_cities

# class EuDateFormField(forms.DateField):
#     def __init__(self, *args, **kwargs):
#         kwargs.update({'input_formats': ("%d.%m.%Y",)})
#         super(EuDateFormField, self).__init__(*args, **kwargs)
#
# class EuDateField(models.DateField):
#     def formfield(self, **kwargs):
#         kwargs.update({'form_class': EuDateFormField})
#
#         return super(EuDateField, self).formfield(**kwargs)

def validate_date(date):
    if date > timezone.now().date():
        raise ValidationError("Date cannot exceed today!")

# def validate_form(date):
#     if

class Organization(models.Model):
    organization_id = models.AutoField(db_column='OrganizationID', primary_key=True)  # Field name made lowercase.
    organization_name = models.CharField(db_column='OrganizationName', max_length=255, unique=True)  # Field name made lowercase.
    date_of_establishment = models.DateField(db_column='DateOfEstablishment', blank=True, null=True, validators=[validate_date], help_text='DD-MM-YYYY')
    # date_of_establishment = testFeild(db_column='DateOfEstablishment', blank=True, null=True)

    # countries_name = get_countries_name()
    #     #
    #     # cities_name = get_cities_name()
    # print(cities_name)


    country = models.ForeignKey('city_country.Country', on_delete=models.SET_NULL, db_column='Country', max_length=255,blank=True, null=True)  # choices=countries_name)  # Field na
    city = ChainedForeignKey('city_country.City', chained_field="country", chained_model_field="countryid", on_delete=models.DO_NOTHING, db_column='City')
                             # max_length=255, blank=True, null=True) #choices=cities_name)  # Field name made lowercase.

    # city = models.ForeignKey('city_country.City', on_delete=models.SET_NULL, db_column='City', max_length=255, blank=True, null=True)

    revenue = models.IntegerField(db_column='Revenue', blank=True, null=True)  # Field name made lowercase.
    it_employee_scale = models.IntegerField(db_column='ITEmployeeScale', blank=True, null=True)  # Field name made lowercase.
    employee_scale = models.IntegerField(db_column='EmployeeScale', blank=True, null=True)  # Field name made lowercase.

    # country = models.ForeignKey('city_country.Country', on_delete=models.SET_NULL, db_column='Country', max_length=255, blank=True, null=True)# choices=countries_name)  # Field name made lowercase.
    # print(country)

    sector = models.ForeignKey('sector.Sector', on_delete=models.SET_NULL, db_column='Sector', blank=True, null=True)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.
    is_valid = models.BooleanField(db_column='isValid', blank=False, null=False, help_text='Please mark this place if this record is valid')

    # gc = geonamescache.GeonamesCache()
    # cities = gc.get_cities()

    class Meta:
        managed = False
        db_table = 'Organization'

    def __str__(self):
        return self.organization_name


# class Country(models.Model):
#
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name
#
#
# class City(models.Model):
#
#     name = models.CharField(max_length=200)
#     country = models.ForeignKey('Country', models.DO_NOTHING, db_column='provience_id')
#
#     def __str__(self):
#         return self.name



