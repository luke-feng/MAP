from django.db import models
from organization.models import Organization
from sector.models import Sector
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class UserInfo(models.Model):
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=255)  # Field name made lowercase.
    userfirstname = models.CharField(db_column='UserFirstName', max_length=255)  # Field name made lowercase.
    userlastname = models.CharField(db_column='UserLastName', max_length=255)
    useremail = models.CharField(db_column='UserEmail', max_length=255)  # Field name made lowercase.
    userscale = models.IntegerField(db_column='UserScale', blank=True, null=True)  # Field name made lowercase.  # Field name made lowercase.
    sectorid = models.ForeignKey('sector.Sector', on_delete=models.SET_NULL, db_column='SectorID', blank=True, null=True)  # Field name made lowercase.
    organizationid = ChainedForeignKey('organization.Organization', chained_field="sectorid", chained_model_field="sector", on_delete=models.SET_NULL,
                                              db_column='OrganizationID', blank=True, null=True)
    modifytime = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.

    country = models.ForeignKey('city_country.Country', on_delete=models.SET_NULL, db_column='Country', max_length=255,
                                blank=True, null=True)  # choices=countries_name)  # Field na
    city = ChainedForeignKey('city_country.City', chained_field="country", chained_model_field="countryid",
                             on_delete=models.SET_NULL, db_column='City', blank=True, null=True)

    postal_code = models.IntegerField(db_column='Postalcode', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', blank=True, null=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserInfo'

    def __str__(self):
        return self.userfirstname+" "+self.userlastname
