from django.db import models

# Create your models here.

class City(models.Model):
    cityid = models.IntegerField(db_column='CityID', primary_key=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=128)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=128)  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'City'

    def __str__(self):
        return self.cityname

class Country(models.Model):
    countryid = models.IntegerField(db_column='CountryID', primary_key=True)  # Field name made lowercase.
    countryname = models.CharField(db_column='CountryName', max_length=128)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Country'

    def __str__(self):
        return self.countryname
