from django.contrib import admin
from sector.models import Sector

def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper

class SectorAdmin(admin.ModelAdmin):
    search_fields = ['sector_name']
    list_display = ('sector_name', 'modify_time', 'is_valid')
    field = ('sector_name', 'is_valid')
    list_filter =(('is_valid', custom_titled_filter('Status')),)

admin.site.register(Sector, SectorAdmin)
