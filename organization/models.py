import django.utils.timezone as timezone

from django.core.exceptions import ValidationError
from django.db import models
import geonamescache
from smart_selects.db_fields import ChainedForeignKey
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from city_country.models import City, Country
from sector.models import Sector

# Create your models here.

def validate_date(date):
    if date > timezone.now().date():
        raise ValidationError("Date cannot exceed today!")


class Organization(models.Model):
    organization_id = models.AutoField(db_column='OrganizationID', primary_key=True)  # Field name made lowercase.
    organization_name = models.CharField(db_column='OrganizationName', max_length=255, unique=True)  # Field name made lowercase.
    date_of_establishment = models.DateField(db_column='DateOfEstablishment', blank=True, null=True, validators=[validate_date], help_text='DD-MM-YYYY')


    country = models.ForeignKey('city_country.Country', on_delete=models.SET_NULL, db_column='Country', max_length=255,blank=True, null=True)
    city = ChainedForeignKey('city_country.City', chained_field="country", chained_model_field="countryid", on_delete=models.DO_NOTHING, db_column='City')

    revenue = models.IntegerField(db_column='Revenue', blank=True, null=True)  # Field name made lowercase.
    it_employee_scale = models.IntegerField(db_column='ITEmployeeScale', blank=True, null=True)  # Field name made lowercase.
    employee_scale = models.IntegerField(db_column='EmployeeScale', blank=True, null=True)  # Field name made lowercase.

    sector = models.ForeignKey('sector.Sector', on_delete=models.SET_NULL, db_column='Sector', blank=True, null=True)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.
    is_valid = models.BooleanField(db_column='isValid', blank=False, null=False, help_text='Please mark this place if this record is valid')

    class Meta:
        managed = False
        db_table = 'Organization'

    def __str__(self):
        return self.organization_name

