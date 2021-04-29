from django.db import models

# Create your models here.

class Measuretype(models.Model):
    measure_type_id = models.AutoField(db_column='MeasureTypeID', primary_key=True)  # Field name made lowercase.
    measure_name = models.CharField(db_column='MeasureName', max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.
    reduced_vulnerability_defult = models.FloatField(db_column='ReducedVulnerabilityDefault', blank=True, null=True)
    reduced_l1_rate_default = models.FloatField(db_column='ReducedL1RateDefault', blank=True, null=True)
    reduced_l2_rate_default = models.FloatField(db_column='ReducedL2RateDefault', blank=True, null=True)
    is_valid = models.BooleanField(db_column='isValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MeasureType'

    def __str__(self):
        return self.measure_name
