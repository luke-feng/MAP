from django.db import models
from information_sharing.models import Incidentcategory
from measure_type.models import Measuretype

# Create your models here.
class Measures(models.Model):
    measure_id = models.AutoField(db_column='MeasureID', primary_key=True)  # Field name made lowercase.
    user_id = models.ForeignKey('user_info.UserInfo', on_delete=models.CASCADE, db_column='UserID')  # Field name made lowercase.
    organization_id = models.ForeignKey('organization.Organization', on_delete=models.CASCADE,
                                        db_column='OrganizationID', blank=True, null=True)  # Field name made lowercase.
    measure_type_id = models.ForeignKey('measure_type.Measuretype',  on_delete=models.CASCADE, db_column='MeasureTypeID')  # Field name made lowercase.
    measure_description = models.TextField(db_column='MeasureDescription', blank=True, null=True)  # Field name made lowercase.
    rosi = models.TextField(db_column='ROSI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    npv = models.TextField(db_column='NPV', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    time_period = models.IntegerField(db_column='TimePeriod', blank=True, null=True)  # Field name made lowercase.
    initial_cost = models.TextField(db_column='InitialCost', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    annual_upgrade = models.TextField(db_column='AnnualUpgrade', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    annual_maintenance = models.TextField(db_column='AnnualMaintenance', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_cost = models.TextField(db_column='TotalCost', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reduced_vulnerability = models.TextField(db_column='ReducedVulnerability', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    insurance_amount = models.TextField(db_column='InsuranceAmount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    times_of_attack = models.IntegerField(db_column='TimesofAttack', blank=True, null=True)  # Field name made lowercase.
    times_of_success_attack = models.IntegerField(db_column='TimesofSuccessAttack', blank=True, null=True)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.
    incident_category = models.ForeignKey('information_sharing.Incidentcategory', models.DO_NOTHING, db_column='IncidentCategory', blank=True, null=True)  # Field name made lowercase.
    vulnerability_without_measure = models.TextField(db_column='VulnerabilityWithoutMeasure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reduced_l1_rate = models.TextField(db_column='ReducedL1Rate', blank=True, null=True)
    reduced_l2_rate = models.TextField(db_column='ReducedL2Rate', blank=True, null=True)
    discount_rate = models.TextField(db_column='DiscountRate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Measures'
