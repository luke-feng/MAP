from django.db import models

# Create your models here.


class Assettype(models.Model):
    asset_type_id = models.AutoField(db_column='AssetTypeID', primary_key=True)  # Field name made lowercase.
    asset_type = models.CharField(db_column='AssetType', max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.
    # is_valid = models.TextField(db_column='isValid', blank=True, null=True)  # Field name made lowercase.
    is_valid = models.BooleanField(db_column='isValid', blank=True, null=True, default=True)

    class Meta:
        managed = False
        db_table = 'AssetType'

        verbose_name = "asset type"

        verbose_name_plural = "asset types"

    def __str__(self):
        return self.asset_type

class Attackerinfrastructure(models.Model):
    attacker_infrastructure_id = models.AutoField(db_column='AttackerInfrastructureID', primary_key=True)  # Field name made lowercase.
    attacker_infrastructure = models.CharField(db_column='AttackerInfrastructure', max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.
    is_valid = models.BooleanField(db_column='isValid', blank=True, null=True, default=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AttackerInfrastructure'

        verbose_name = "Attacker Infrastructure"

        verbose_name_plural = "Attacker Infrastructures"

    def __str__(self):
        return self.attacker_infrastructure

class Attackertool(models.Model):
    attacker_tool_id = models.AutoField(db_column='AttackerToolID', primary_key=True)  # Field name made lowercase.
    attacker_tool = models.CharField(db_column='AttackerTool', max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False) # Field name made lowercase. This field type is a guess.
    is_valid = models.BooleanField(db_column='isValid', blank=True, null=True, default=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AttackerTool'

        verbose_name = "Attacker Tool"

        verbose_name_plural = "Attacker Tools"

    def __str__(self):
        return self.attacker_tool

class Impactrating(models.Model):
    impact_rating_id = models.AutoField(db_column='ImpactRatingID', primary_key=True)  # Field name made lowercase.
    impact_rating = models.CharField(db_column='ImpactRating', max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ImpactRating'

        verbose_name = "Impact Rating"

        verbose_name_plural = "Impact Ratings"

    def __str__(self):
        return self.impact_rating

class Incidentcategory(models.Model):
    incident_category_id = models.AutoField(db_column='IncidentCategoryID', primary_key=True)  # Field name made lowercase.
    incident_category = models.CharField(db_column='IncidentCategory', max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'IncidentCategory'

        verbose_name = "IncidentCategory"

        verbose_name_plural = "Incident Categories"

    def __str__(self):
        return self.incident_category

class Incidenteffect(models.Model):
    incident_effect_id = models.AutoField(db_column='IncidentEffectID', primary_key=True)  # Field name made lowercase.
    incident_effect = models.CharField(db_column='IncidentEffect', max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False) # Field name made lowercase. This field type is a guess.
    is_valid = models.BooleanField(db_column='isValid', blank=True, null=True, default=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IncidentEffect'

        verbose_name = "Incident Effect"

        verbose_name_plural = "Incident Effects"

    def __str__(self):
        return self.incident_effect

class Lossproperty(models.Model):
    loss_property_id = models.AutoField(db_column='LossPropertyID', primary_key=True)  # Field name made lowercase.
    loss_property = models.CharField(db_column='LossProperty', max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.
    is_valid =models.BooleanField(db_column='isValid', blank=True, null=True, default=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LossProperty'

        verbose_name = "Loss Property"

        verbose_name_plural = "Loss Properties"

    def __str__(self):
        return self.loss_property

class Malwaretype(models.Model):
    malware_type_id = models.AutoField(db_column='MalwareTypeID', primary_key=True)  # Field name made lowercase.
    malware_type = models.CharField(db_column='MalwareType', max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.
    is_valid = models.BooleanField(db_column='isValid', blank=True, null=True, default=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MalwareType'

        verbose_name = "Malware Type"

        verbose_name_plural = "Malware Types"

    def __str__(self):
        return self.malware_type


class Securitycompromise(models.Model):
    security_compromise_id = models.AutoField(db_column='SecurityCompromiseID', primary_key=True)  # Field name made lowercase.
    security_compromise = models.CharField(db_column='SecurityCompromise', blank=True, null=True, max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SecurityCompromise'

        verbose_name = "Security Compromise"

        verbose_name_plural = "Security Compromise"

    def __str__(self):
        return self.security_compromise


class Systemtype(models.Model):
    system_type_id = models.AutoField(db_column='SystemTypeID', primary_key=True)  # Field name made lowercase.
    system_type = models.CharField(db_column='SystemType', max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.
    is_valid = models.BooleanField(db_column='isValid', blank=True, null=True, default=True)   # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SystemType'

        verbose_name = "System Type"

        verbose_name_plural = "System Types"

    def __str__(self):
        return self.system_type


class Threatactortype(models.Model):
    threat_actor_type_id = models.AutoField(db_column='ThreatActorTypeID', primary_key=True)  # Field name made lowercase.
    threat_actor_type = models.CharField(db_column='ThreatActorType', max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.
    is_valid = models.BooleanField(db_column='isValid', blank=True, null=True, default=True)   # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ThreatActorType'

        verbose_name = "Threat Actor Type"

        verbose_name_plural = "Threat Actor Types"

    def __str__(self):
        return self.threat_actor_type

class Discoverymethod(models.Model):
    discovery_method_id = models.AutoField(db_column='DiscoveryMethodID', primary_key=True)  # Field name made lowercase.
    discovery_method = models.CharField(db_column='DiscoveryMethod', max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.
    is_valid = models.BooleanField(db_column='isValid', blank=True, null=True, default=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DiscoveryMethod'

        verbose_name = "Discovery Method"

        verbose_name_plural = "Discovery Methods"

    def __str__(self):
        return self.discovery_method

class Lossduration(models.Model):
    loss_duration_id = models.AutoField(db_column='LossDurationID', primary_key=True)  # Field name made lowercase.
    loss_duration = models.CharField(db_column='LossDuration', max_length=128)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'LossDuration'

        verbose_name = "Loss Duration"

        verbose_name_plural = "Loss Duration"

    def __str__(self):
        return self.loss_duration




