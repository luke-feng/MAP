from django.db import models
from information_sharing.models import Assettype, Systemtype, Malwaretype, Attackertool, Threatactortype, Incidenteffect,\
    Lossproperty, Attackerinfrastructure, Discoverymethod

# Create your models here.

class Attackinformation(models.Model):


    attack_id = models.OneToOneField('attack_features.Attackfeatures', on_delete=models.CASCADE, db_column='AttackID', primary_key=True)  # Field name made lowercase.

    user_id = models.ForeignKey('user_info.UserInfo', on_delete=models.SET_NULL, db_column='UserID', blank=True, null=True)  # Field name made lowercase.

    organization_id = models.ForeignKey('organization.Organization', on_delete=models.SET_NULL,
                                        db_column='OrganizationID', blank=True, null=True)
    sector_id = models.ForeignKey('sector.Sector', on_delete=models.SET_NULL, db_column='SectorID', blank=True,
                                  null=True)
    costofequipmentreplacement = models.FloatField(db_column='CostofEquipmentReplacement', blank=True, null=True, default=0.0)  # Field name made lowercase. This field type is a guess.
    costofrepair = models.FloatField(db_column='CostofRepair', blank=True, null=True, default=0.0)  # Field name made lowercase. This field type is a guess.
    corporate_income_loss = models.FloatField(db_column='CorporateIncomeLoss', blank=True, null=True, default=0.0)  # Field name made lowercase. This field type is a guess.
    organization_productive_loss = models.FloatField(db_column='OrganizationProductiveLoss', blank=True, null=True, default=0.0)  # Field name made lowercase. This field type is a guess.
    sla_loss = models.FloatField(db_column='SLALoss', blank=True, null=True, default=0.0)  # Field name made lowercase. This field type is a guess.
    indirect_loss = models.FloatField(db_column='IndirectLoss', blank=True, null=True, default=0.0)  # Field name made lowercase. This field type is a guess.
    impact_rating = models.ForeignKey('information_sharing.Impactrating', on_delete=models.SET_NULL, db_column='ImpactRating', blank=True, null=True)
    incident_category = models.ForeignKey('information_sharing.Incidentcategory', on_delete=models.SET_NULL, db_column='IncidentCategory', blank=True, null=True)
    security_compromise = models.ForeignKey('information_sharing.Securitycompromise', on_delete=models.SET_NULL, db_column='SecurityCompromise', blank=True, null=True)
    loss_duration = models.ForeignKey('information_sharing.Lossduration', on_delete=models.SET_NULL, db_column='LossDuration', blank=True, null=True)  # Field name made lowercase.
    incident_effect = models.ManyToManyField(Incidenteffect, db_column='IncidentEffect', through='Attackinformation2Incidenteffect', through_fields=('attack_information','incident_effect'), blank=True, null=True)  # Field name made lowercase.
    loss_property = models.ManyToManyField(Lossproperty, db_column='LossProperty', through='Attackinformation2Lossproperty', through_fields=('attack_information','loss_property'),blank=True, null=True)  # Field name made lowercase.
    attacker_infrastructure = models.ManyToManyField(Attackerinfrastructure, db_column='AttackerInfrastructure',through='Attackinformation2Attackerinfrastructure', through_fields=('attack_information','attacker_infrastructure'), blank=True, null=True)  # Field name made lowercase.
    threat_actor_type = models.ManyToManyField(Threatactortype, through='Attackinformation2Threatactortype',through_fields=('attack_information','threat_actor_type'), db_column='ThreatActorType', blank=True, null=True)  # Field name made lowercase.
    attacker_tool = models.ManyToManyField(Attackertool, db_column='AttackerTool', through='Attackinformation2Attackertool', through_fields=('attack_information','attacker_tool'))  # Field name made lowercase.
    malware_type = models.ManyToManyField(Malwaretype, db_column='MalwareType', through='Attackinformation2Malwaretype', through_fields=('attack_information','malware_type'))  # Field name made lowercase.
    malicious_e_mail = models.TextField(db_column='MaliciousE-mail', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    ip_watchlist = models.TextField(db_column='IPWatchlist', blank=True, null=True, max_length=255)  # Field name made lowercase. This field type is a guess.
    file_hash_watchlist = models.TextField(db_column='FileHashWatchlist', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    domain_watchlist = models.TextField(db_column='DomainWatchlist', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    url_watchlist = models.TextField(db_column='URLWatchlist', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    system_type = models.ManyToManyField(Systemtype, db_column='SystemType', through='Attackinformation2Systemtype', through_fields=('attack_information','system_type'))  # Field name made lowercase.
    asset_type = models.ManyToManyField(Assettype, db_column='AssetType', through='Attackinformation2Assettype', through_fields=('attack_information','asset_type'))
    discovery_method = models.ManyToManyField(Discoverymethod, db_column='DiscoveryMethod', through='Attackinformation2Discoverymethod', through_fields=('attack_information','discovery_method'), blank=True, null=True)  # Field name made lowercase.
    l1 = models.FloatField(db_column='L1', blank=True, null=True, default=0.0)  # Field name made lowercase. This field type is a guess.
    l2 = models.FloatField(db_column='L2', blank=True, null=True, default=0.0)  # Field name made lowercase. This field type is a guess.
    l3 = models.FloatField(db_column='L3', blank=True, null=True, default=0.0)  # Field name made lowercase. This field type is a guess.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.
    discount_rate = models.TextField(db_column='DiscountRate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'AttackInformation'

    def __str__(self):
        return self.attack_id

class Attackinformation2Assettype(models.Model):
    attack_information = models.ForeignKey(Attackinformation, to_field='attack_id', on_delete=models.CASCADE)
    asset_type = models.ForeignKey(Assettype, to_field='asset_type_id', on_delete=models.CASCADE)
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)

class Attackinformation2Systemtype(models.Model):
    attack_information = models.ForeignKey(Attackinformation, to_field='attack_id', on_delete=models.CASCADE)
    system_type = models.ForeignKey(Systemtype, to_field='system_type_id', on_delete=models.CASCADE)
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)

class Attackinformation2Malwaretype(models.Model):
    attack_information = models.ForeignKey(Attackinformation, to_field='attack_id', on_delete=models.CASCADE)
    malware_type = models.ForeignKey(Malwaretype, to_field='malware_type_id', on_delete=models.CASCADE)
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)

class Attackinformation2Attackertool(models.Model):
    attack_information = models.ForeignKey(Attackinformation, to_field='attack_id', on_delete=models.CASCADE)
    attacker_tool = models.ForeignKey(Attackertool, to_field='attacker_tool_id', on_delete=models.CASCADE)
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)

class Attackinformation2Threatactortype(models.Model):
    attack_information = models.ForeignKey(Attackinformation, to_field='attack_id', on_delete=models.CASCADE)
    threat_actor_type = models.ForeignKey(Threatactortype, to_field='threat_actor_type_id', on_delete=models.CASCADE)
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)

class Attackinformation2Attackerinfrastructure(models.Model):
    attack_information = models.ForeignKey(Attackinformation, to_field='attack_id', on_delete=models.CASCADE)
    attacker_infrastructure = models.ForeignKey(Attackerinfrastructure, to_field='attacker_infrastructure_id', on_delete=models.CASCADE)
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)

class Attackinformation2Lossproperty(models.Model):
    attack_information = models.ForeignKey(Attackinformation, to_field='attack_id', on_delete=models.CASCADE)
    loss_property = models.ForeignKey(Lossproperty, to_field='loss_property_id', on_delete=models.CASCADE)
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)

class Attackinformation2Incidenteffect(models.Model):
    attack_information = models.ForeignKey(Attackinformation, to_field='attack_id', on_delete=models.CASCADE)
    incident_effect = models.ForeignKey(Incidenteffect, to_field='incident_effect_id', on_delete=models.CASCADE)
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)

class Attackinformation2Discoverymethod(models.Model):
    attack_information = models.ForeignKey(Attackinformation, to_field='attack_id', on_delete=models.CASCADE)
    discovery_method = models.ForeignKey(Discoverymethod, to_field='discovery_method_id', on_delete=models.CASCADE)
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)
