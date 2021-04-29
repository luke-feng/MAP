from django.db import models
from unixtimestampfield.fields import UnixTimeStampField

# Create your models here.
#
class Sector(models.Model):
    sectorid = models.AutoField(db_column='SectorID', primary_key=True)  # Field name made lowercase.
    sector_name = models.CharField(db_column='SectorName', max_length=128, unique=True)
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)
    is_valid = models.BooleanField(db_column='isValid', blank=False, null=False, help_text='Please mark this place if this record is valid')

    class Meta:
        managed = False
        db_table = 'Sector'

    def __str__(self):
        return self.sector_name
