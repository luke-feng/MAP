from django.contrib import admin
from .models import UserInfo
from sector.models import Sector

# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    # form = BankcardsForm
    # search_fields = ['username']
    fields = ('userid','userfirstname', 'userlastname', 'useremail', 'userscale', 'sectorid', 'organizationid')
    list_display = ('userid','userfirstname', 'userlastname', 'modifytime')
    # list_filter = ('sector','is_valid',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sectorid":
            kwargs["queryset"] = Sector.objects.filter(is_valid=True)
        return super(UserInfoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(UserInfo, UserInfoAdmin)
