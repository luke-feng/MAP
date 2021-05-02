from django.db import models
import django.utils.timezone as timezone
from django.core.exceptions import ValidationError

# Create your models here.

class Attackfeatures(models.Model):

    attack_id = models.CharField(db_column='AttackID', primary_key=True, max_length=255)  # Field name made lowercase.

    start_time_stamp = models.DateTimeField(db_column='StartTimeStamp', blank=True, null=True)

    end_time_stamp = models.DateTimeField(db_column='EndTimeStamp', blank=True, null=True)

    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    nr_of_ip_packets = models.IntegerField(db_column='NrOfIPpackets', blank=True, null=True)  # Field name made lowercase.
    attack_size_in_bytes = models.IntegerField(db_column='AttackSizeInBytes', blank=True, null=True)  # Field name made lowercase.
    nr_of_src_ips = models.IntegerField(db_column='NrOfSrcIps', blank=True, null=True)  # Field name made lowercase.
    nr_of_dst_ips = models.IntegerField(db_column='NrOfDstIps', blank=True, null=True)  # Field name made lowercase.
    top_5_src_ip = models.TextField(db_column='Top5SrcIP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nr_of_src_port = models.IntegerField(db_column='NrOfSrcPort', blank=True, null=True)  # Field name made lowercase.
    nr_of_ds_port = models.IntegerField(db_column='NrOfDsPort', blank=True, null=True)  # Field name made lowercase.
    top_20_des_port = models.TextField(db_column='Top20DesPort', blank=True, null=True)  # Field name made lowercase.
    top_http_verb = models.TextField(db_column='TopHttpVerb', blank=True, null=True)  # Field name made lowercase.
    top_http_endpoint = models.TextField(db_column='TopHttpEndpoint', blank=True, null=True)  # Field name made lowercase.
    top_browser_os = models.TextField(db_column='TopBrowserOS', blank=True, null=True)  # Field name made lowercase.
    top_device = models.TextField(db_column='TopDevice', blank=True, null=True)  # Field name made lowercase.
    modify_time = models.DateTimeField(db_column='ModifyTime', auto_now=True, null=True, blank=True, editable=False)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'AttackFeatures'

    def __str__(self):
        return self.attack_id
