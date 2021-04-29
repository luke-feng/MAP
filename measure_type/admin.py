from django.contrib import admin
from .models import Measuretype
# Register your models here.

class MeasuretypeAdmin(admin.ModelAdmin):
    search_fields = ['measure_name']
    fields = ('measure_name', 'reduced_vulnerability_defult', 'reduced_l1_rate_default', 'reduced_l2_rate_default','is_valid')
    list_display = ('measure_name', 'modify_time','is_valid')
    list_filter = ('is_valid',)

admin.site.register(Measuretype,MeasuretypeAdmin)
