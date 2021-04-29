# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Application(models.Model):
    applicationid = models.AutoField(db_column='ApplicationID')  # Field name made lowercase.
    fisrtname = models.TextField(db_column='FisrtName', blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    organizationid = models.IntegerField(db_column='OrganizationID', blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.TextField(db_column='EmailAddress', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID', blank=True, null=True)  # Field name made lowercase.
    postalcode = models.IntegerField(db_column='Postalcode', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    sectorid = models.IntegerField(db_column='SectorID', blank=True, null=True)  # Field name made lowercase.
    userscale = models.TextField(db_column='UserScale', blank=True, null=True)  # Field name made lowercase.
    revenue = models.TextField(db_column='Revenue', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    processed = models.BooleanField(db_column='Processed', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Application'


class Assettype(models.Model):
    assettypeid = models.AutoField(db_column='AssetTypeID', primary_key=True)  # Field name made lowercase.
    assettype = models.CharField(db_column='AssetType', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isvalid = models.TextField(db_column='isValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AssetType'


class Attackfeatures(models.Model):
    attackid = models.CharField(db_column='AttackID', primary_key=True)  # Field name made lowercase.
    starttimestamp = models.TextField(db_column='StartTimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    endtimestamp = models.TextField(db_column='EndTimeStamp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    nrofippackets = models.IntegerField(db_column='NrOfIPpackets', blank=True, null=True)  # Field name made lowercase.
    attacksizeinbytes = models.IntegerField(db_column='AttackSizeInBytes', blank=True, null=True)  # Field name made lowercase.
    nrofsrcips = models.IntegerField(db_column='NrOfSrcIps', blank=True, null=True)  # Field name made lowercase.
    nrofdstips = models.IntegerField(db_column='NrOfDstIps', blank=True, null=True)  # Field name made lowercase.
    top5srcip = models.TextField(db_column='Top5SrcIP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nrofsrcport = models.IntegerField(db_column='NrOfSrcPort', blank=True, null=True)  # Field name made lowercase.
    nrofdsport = models.IntegerField(db_column='NrOfDsPort', blank=True, null=True)  # Field name made lowercase.
    top20desport = models.TextField(db_column='Top20DesPort', blank=True, null=True)  # Field name made lowercase.
    tophttpverb = models.TextField(db_column='TopHttpVerb', blank=True, null=True)  # Field name made lowercase.
    tophttpendpoint = models.TextField(db_column='TopHttpEndpoint', blank=True, null=True)  # Field name made lowercase.
    topbrowseros = models.TextField(db_column='TopBrowserOS', blank=True, null=True)  # Field name made lowercase.
    topdevice = models.TextField(db_column='TopDevice', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'AttackFeatures'


class Attackinformation(models.Model):
    attackid = models.CharField(db_column='AttackID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    organizationid = models.IntegerField(db_column='OrganizationID')  # Field name made lowercase.
    sectorid = models.IntegerField(db_column='SectorID')  # Field name made lowercase.
    timetorepair_without = models.IntegerField(db_column='TimetoRepair_without', blank=True, null=True)  # Field name made lowercase.
    timetodetect_without = models.IntegerField(db_column='TimetoDetect_without', blank=True, null=True)  # Field name made lowercase.
    costofequipmentreplacement = models.TextField(db_column='CostofEquipmentReplacement', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    costofrepair = models.TextField(db_column='CostofRepair', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    corporateincomeloss = models.TextField(db_column='CorporateIncomeLoss', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    organizationproductiveloss = models.TextField(db_column='OrganizationProductiveLoss', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    slaloss = models.TextField(db_column='SLALoss', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    indirectloss = models.TextField(db_column='IndirectLoss', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    impactrating = models.IntegerField(db_column='ImpactRating', blank=True, null=True)  # Field name made lowercase.
    incidenteffect = models.IntegerField(db_column='IncidentEffect', blank=True, null=True)  # Field name made lowercase.
    securitycompromise = models.IntegerField(db_column='SecurityCompromise', blank=True, null=True)  # Field name made lowercase.
    lossduration = models.IntegerField(db_column='LossDuration', blank=True, null=True)  # Field name made lowercase.
    lossproperty = models.IntegerField(db_column='LossProperty', blank=True, null=True)  # Field name made lowercase.
    attackerinfrastructure = models.IntegerField(db_column='AttackerInfrastructure', blank=True, null=True)  # Field name made lowercase.
    threatactortype = models.IntegerField(db_column='ThreatActorType', blank=True, null=True)  # Field name made lowercase.
    attackertool = models.IntegerField(db_column='AttackerTool', blank=True, null=True)  # Field name made lowercase.
    malwaretype = models.IntegerField(db_column='MalwareType', blank=True, null=True)  # Field name made lowercase.
    maliciouse_mail = models.TextField(db_column='MaliciousE-mail', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    ipwatchlist = models.TextField(db_column='IPWatchlist', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    filehashwatchlist = models.TextField(db_column='FileHashWatchlist', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    domainwatchlist = models.TextField(db_column='DomainWatchlist', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    urlwatchlist = models.TextField(db_column='URLWatchlist', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hostcharacteristics = models.TextField(db_column='HostCharacteristics', blank=True, null=True)  # Field name made lowercase.
    incidentcategory = models.IntegerField(db_column='IncidentCategory', blank=True, null=True)  # Field name made lowercase.
    systemtype = models.IntegerField(db_column='SystemType', blank=True, null=True)  # Field name made lowercase.
    assettype = models.IntegerField(db_column='AssetType', blank=True, null=True)  # Field name made lowercase.
    discoverymethod = models.IntegerField(db_column='DiscoveryMethod', blank=True, null=True)  # Field name made lowercase.
    l1 = models.TextField(db_column='L1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    l2 = models.TextField(db_column='L2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    l3 = models.TextField(db_column='L3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    discountrate = models.TextField(db_column='DiscountRate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'AttackInformation'


class Attackerinfrastructure(models.Model):
    attackerinfrastructureid = models.AutoField(db_column='AttackerInfrastructureID', primary_key=True)  # Field name made lowercase.
    attackerinfrastructure = models.CharField(db_column='AttackerInfrastructure', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isvalid = models.TextField(db_column='isValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AttackerInfrastructure'


class Attackertool(models.Model):
    attackertoolid = models.AutoField(db_column='AttackerToolID', primary_key=True)  # Field name made lowercase.
    attackertool = models.CharField(db_column='AttackerTool', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isvalid = models.TextField(db_column='isValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AttackerTool'


class City(models.Model):
    cityid = models.AutoField(db_column='CityID')  # Field name made lowercase.
    cityname = models.CharField(db_column='CityName')  # Field name made lowercase.
    countrycode = models.IntegerField(db_column='CountryCode')  # Field name made lowercase.
    countryid = models.IntegerField(db_column='CountryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'City'


class Country(models.Model):
    countryid = models.AutoField(db_column='CountryID')  # Field name made lowercase.
    countryname = models.CharField(db_column='CountryName')  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Country'


class Discoverymethod(models.Model):
    discoverymethodid = models.AutoField(db_column='DiscoveryMethodID', primary_key=True)  # Field name made lowercase.
    discoverymethod = models.CharField(db_column='DiscoveryMethod', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'DiscoveryMethod'


class Impactrating(models.Model):
    impactratingid = models.AutoField(db_column='ImpactRatingID', primary_key=True)  # Field name made lowercase.
    impactrating = models.CharField(db_column='ImpactRating', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ImpactRating'


class Incidentcategory(models.Model):
    incidentcategoryid = models.AutoField(db_column='IncidentCategoryID', primary_key=True)  # Field name made lowercase.
    incidentcategory = models.CharField(db_column='IncidentCategory', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'IncidentCategory'


class Incidenteffect(models.Model):
    incidenteffectid = models.AutoField(db_column='IncidentEffectID', primary_key=True)  # Field name made lowercase.
    incidenteffect = models.CharField(db_column='IncidentEffect', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isvalid = models.TextField(db_column='isValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IncidentEffect'


class Lossduration(models.Model):
    lossdurationid = models.AutoField(db_column='LossDurationID', primary_key=True)  # Field name made lowercase.
    lossduration = models.CharField(db_column='LossDuration', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'LossDuration'


class Lossproperty(models.Model):
    losspropertyid = models.AutoField(db_column='LossPropertyID', primary_key=True)  # Field name made lowercase.
    lossproperty = models.CharField(db_column='LossProperty', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isvalid = models.TextField(db_column='isValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LossProperty'


class Malwaretype(models.Model):
    malwaretypeid = models.AutoField(db_column='MalwareTypeID', primary_key=True)  # Field name made lowercase.
    malwaretype = models.CharField(db_column='MalwareType', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isvalid = models.TextField(db_column='isValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MalwareType'


class Measuretype(models.Model):
    measuretypeid = models.AutoField(db_column='MeasureTypeID', primary_key=True)  # Field name made lowercase.
    measurename = models.CharField(db_column='MeasureName', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'MeasureType'


class Measures(models.Model):
    measureid = models.AutoField(db_column='MeasureID', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
    organizationid = models.IntegerField(db_column='OrganizationID')  # Field name made lowercase.
    measuretypeid = models.IntegerField(db_column='MeasureTypeID')  # Field name made lowercase.
    measuredescription = models.TextField(db_column='MeasureDescription', blank=True, null=True)  # Field name made lowercase.
    rosi = models.TextField(db_column='ROSI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    npv = models.TextField(db_column='NPV', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    irr = models.TextField(db_column='IRR', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rank = models.IntegerField(db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    timeperiod = models.IntegerField(db_column='TimePeriod', blank=True, null=True)  # Field name made lowercase.
    initialcost = models.TextField(db_column='InitialCost', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    annualupgrade = models.TextField(db_column='AnnualUpgrade', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    annualmaintenance = models.TextField(db_column='AnnualMaintenance', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    totalcost = models.TextField(db_column='TotalCost', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reducedvulnerability = models.TextField(db_column='ReducedVulnerability', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    insuranceamount = models.TextField(db_column='InsuranceAmount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timesofattack = models.IntegerField(db_column='TimesofAttack', blank=True, null=True)  # Field name made lowercase.
    timesofsuccessattack = models.IntegerField(db_column='TimesofSuccessAttack', blank=True, null=True)  # Field name made lowercase.
    minimumrisk = models.TextField(db_column='MinimumRisk', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    maximumrisk = models.TextField(db_column='MaximumRisk', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    maxonetimeloss = models.TextField(db_column='MaxOnetimeLoss', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    riskwithoutmeasure = models.TextField(db_column='RiskwithoutMeasure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    incidentcategory = models.ForeignKey(Incidentcategory, models.DO_NOTHING, db_column='IncidentCategory', blank=True, null=True)  # Field name made lowercase.
    vulnerabilitywithoutmeasure = models.TextField(db_column='VulnerabilityWithoutMeasure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    losswithoutmeasure = models.TextField(db_column='LossWithoutMeasure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timetodetect_with = models.TextField(db_column='TimetoDetect_with', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timetorepair_with = models.TextField(db_column='TimetoRepair_with', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Measures'


class Organization(models.Model):
    organizationid = models.AutoField(db_column='OrganizationID')  # Field name made lowercase.
    organizationname = models.CharField(db_column='OrganizationName', max_length=255)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    revenue = models.IntegerField(db_column='Revenue', blank=True, null=True)  # Field name made lowercase.
    itemployeescale = models.IntegerField(db_column='ITEmployeeScale', blank=True, null=True)  # Field name made lowercase.
    employeescale = models.IntegerField(db_column='EmployeeScale', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sector = models.IntegerField(db_column='Sector', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dateofestablishment = models.DateField(db_column='DateOfEstablishment', blank=True, null=True)  # Field name made lowercase.
    isvalid = models.BooleanField(db_column='isValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organization'


class Password(models.Model):
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase. This field type is a guess.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Password'


class Sector(models.Model):
    sectorid = models.AutoField(db_column='SectorID')  # Field name made lowercase.
    sectorname = models.TextField(db_column='SectorName')  # Field name made lowercase. This field type is a guess.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isvalid = models.BooleanField(db_column='isValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sector'


class Securitycompromise(models.Model):
    securitycompromiseid = models.AutoField(db_column='SecurityCompromiseID', primary_key=True)  # Field name made lowercase.
    securitycompromise = models.CharField(db_column='SecurityCompromise', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SecurityCompromise'


class Systemtype(models.Model):
    systemtypeid = models.AutoField(db_column='SystemTypeID', primary_key=True)  # Field name made lowercase.
    systemtype = models.CharField(db_column='SystemType', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isvalid = models.TextField(db_column='isValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SystemType'


class Threatactortype(models.Model):
    threatactortypeid = models.AutoField(db_column='ThreatActorTypeID', primary_key=True)  # Field name made lowercase.
    threatactortype = models.CharField(db_column='ThreatActorType', max_length=128)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isvalid = models.TextField(db_column='isValid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ThreatActorType'


class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255)  # Field name made lowercase.
    useremail = models.CharField(db_column='UserEmail', max_length=255)  # Field name made lowercase.
    userscale = models.IntegerField(db_column='UserScale', blank=True, null=True)  # Field name made lowercase.
    organizationid = models.ForeignKey(Organization, models.DO_NOTHING, db_column='OrganizationID', blank=True, null=True)  # Field name made lowercase.
    sectorid = models.ForeignKey(Sector, models.DO_NOTHING, db_column='SectorID', blank=True, null=True)  # Field name made lowercase.
    modifytime = models.TextField(db_column='ModifyTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'User'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
