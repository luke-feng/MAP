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

# class OrganizationAdmin(admin.ModelAdmin):
#     change_form_template = 'record_change_form.html'
#     # list_display = ('organization_name', 'modify_time')
#     # fields = ('organization_name','country','city','revenue',)
#
#     def change_view(self, request, object_id, form_url='', extra_context=None):
#         extra_context = extra_context or {}
#         extra_context['osm_data'] = self.get_dynamic_info()
#         return super(OrganizationAdmin, self).change_view(
#             request, object_id, form_url, extra_context=extra_context,
#         )

# class DateForm(forms.ModelForm):
#     from_date = forms.DateField(widget=AdminDateWidget())
#
# class CustomerAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.DateField: { 'widget': AdminDateWidget },
#     }
#
# class DateSelectorWidget(forms.MultiWidget):
#     def __init__(self, attrs=None):
#         year_now = datetime.datetime.now().year
#         # print (year_now)
#         days = [(day, day) for day in range(1, 32)]
#         months = [(month, month) for month in range(1, 13)]
#         years = [(year, year) for year in range(1700, year_now+1)]
#         widgets = [
#             forms.Select(attrs=attrs, choices=days),
#             forms.Select(attrs=attrs, choices=months),
#             forms.Select(attrs=attrs, choices=years),
#         ]
#         super().__init__(widgets, attrs)
#
#     def decompress(self, value):
#         if isinstance(value, date):
#             return [value.day, value.month, value.year]
#         elif isinstance(value, str):
#             year, month, day = value.split('-')
#             return [day, month, year]
#         return [None, None, None]
#
#     def value_from_datadict(self, data, files, name):
#         day, month, year = super().value_from_datadict(data, files, name)
#         # DateField expects a single string that it can parse into a date.
#         return '{}-{}-{}'.format(year, month, day)
#
# def validate_date(date):
#     if date > timezone.now().date():
#         raise ValidationError("Date cannot be in the past")
#
# class BankcardsForm(forms.ModelForm):
#     # date_of_establishment = forms.DateField(widget=[forms.TextInput(attrs={'placeholder': u'DD-MM-YYY'}, forms.SelectDateWidget(empty_label="Nothing") ] ))
#     date_of_establishment = forms.DateField(widget=DateSelectorWidget, validators=[validate_date,])


    # code = forms.CharField(validators=[bankcode_validate, ], widget=forms.TextInput(attrs={'placeholder': u'输入银行编号'}))





class OrganizationAdmin(admin.ModelAdmin):
    # form = BankcardsForm
    search_fields = ['organization_name']
    fields = ('organization_name', 'date_of_establishment', 'country', 'city', 'revenue', 'it_employee_scale', 'employee_scale', 'sector','is_valid')
    list_display = ('organization_name', 'sector', 'modify_time','is_valid')
    list_filter = ('sector','is_valid',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sector":
            kwargs["queryset"] = Sector.objects.filter(is_valid=True)
        return super(OrganizationAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Organization, OrganizationAdmin)
# admin.site.register(BankcardsForm)
# admin.site.register(City)
# admin.site.register(Country)
