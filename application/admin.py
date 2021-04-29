from django.contrib import admin

# Register your models here.
from application.models import Application


class ApplicationAdmin(admin.ModelAdmin):
    # form = BankcardsForm
    # search_fields = ['organization_name']
    fields = ('first_name', 'last_name', 'email_address', 'password', 'sector_id', 'organization_id',
              'country_id', 'city_id', 'postal_code', 'address', 'user_scale', 'revenue', 'organization_name',
              'date_of_establishment', 'it_employee_scale', 'employee_scale', 'processed')
    list_display = ('application_id', 'modify_time', 'processed')
    list_filter = ('processed',)
    readonly_fields = ('first_name','last_name', 'email_address','password',)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "sector":
    #         kwargs["queryset"] = Application.objects.filter(is_valid=True)
    #     return super(ApplicationAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Application, ApplicationAdmin)
