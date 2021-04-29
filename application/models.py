from django.db import models
from sector.models import Sector
from smart_selects.db_fields import ChainedForeignKey
import django.utils.timezone as timezone

from django.core.exceptions import ValidationError

# Create your models here.
def validate_date(date):
    if date > timezone.now().date():
        raise ValidationError("Date cannot exceed today!")

class Application(models.Model):
    application_id = models.AutoField(db_column='ApplicationID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='FisrtName', blank=True, null=True, max_length=128)  # Field name made lowercase.
    last_name = models.CharField(db_column='LastName', blank=True, null=True, max_length=128)  # Field name made lowercase.
    organization_id = models.ForeignKey('organization.Organization', on_delete=models.SET_NULL, db_column='OrganizationID', blank=True, null=True)
    email_address = models.EmailField(db_column='EmailAddress', blank=True, null=True, max_length=128)  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    country_id = models.ForeignKey('city_country.Country', on_delete=models.SET_NULL, db_column='CountryID', max_length=255,
                                blank=True, null=True)
    city_id = ChainedForeignKey('city_country.City', chained_field="country_id", chained_model_field="countryid",
                             on_delete=models.DO_NOTHING, db_column='CityID')
    postal_code = models.IntegerField(db_column='Postalcode', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', blank=True, null=True, max_length=255)  # Field name made lowercase.
    sector_id = models.ForeignKey('sector.Sector', on_delete=models.SET_NULL, db_column='SectorID', blank=True, null=True)
    user_scale = models.CharField(db_column='UserScale', blank=True, null=True, max_length=128)  # Field name made lowercase.
    revenue = models.CharField(db_column='Revenue', blank=True, null=True, max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.
    processed = models.BooleanField(db_column='Processed', blank=True, null=True, default=False)  # Field name made lowercase.

    organization_name = models.CharField(db_column='OrganizationName', blank=True, null=True, max_length=128)
    date_of_establishment = models.DateField(db_column='DateOfEstablishment', blank=True, null=True, validators=[validate_date],
                     help_text='DD-MM-YYYY')
    it_employee_scale = models.IntegerField(db_column='ITEmployeeScale', blank=True,
                                            null=True)  # Field name made lowercase.
    employee_scale = models.IntegerField(db_column='EmployeeScale', blank=True, null=True)  # Field name made lowercase.



    class Meta:
        managed = False
        db_table = 'Application'

    def __str__(self):
        return str(self.application_id)
