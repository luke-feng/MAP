from django.contrib import admin
from django.core.exceptions import ValidationError

from organization.models import Organization
from django import forms
from sector.models import Sector
from city_country.models import City,Country
from django.contrib.admin.widgets import AdminDateWidget
import django.utils.timezone as timezone
from datetime import date
import datetime


# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
    search_fields = ['organization_name']
    fields = ('organization_name', 'date_of_establishment', 'country', 'city', 'revenue', 'it_employee_scale', 'employee_scale', 'sector','is_valid')
    list_display = ('organization_name', 'sector', 'modify_time','is_valid')
    list_filter = ('sector','is_valid',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sector":
            kwargs["queryset"] = Sector.objects.filter(is_valid=True)
        return super(OrganizationAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Organization, OrganizationAdmin)
