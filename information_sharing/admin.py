from django.contrib import admin
from information_sharing.models import Assettype
from information_sharing.models import Attackerinfrastructure
from information_sharing.models import Attackertool
from information_sharing.models import Impactrating
from information_sharing.models import Incidentcategory
from information_sharing.models import Incidenteffect
from information_sharing.models import Lossproperty
from information_sharing.models import Malwaretype
from information_sharing.models import Securitycompromise
from information_sharing.models import Systemtype
from information_sharing.models import Threatactortype
from information_sharing.models import Discoverymethod
from information_sharing.models import Lossduration


class AssettypeAdmin(admin.ModelAdmin):
    search_fields = ['asset_type']
    list_display = ('asset_type', 'modify_time', 'is_valid')
    list_filter = ('is_valid',)

admin.site.register(Assettype, AssettypeAdmin)
admin.site.register(Attackerinfrastructure)
admin.site.register(Attackertool)
admin.site.register(Incidentcategory)
admin.site.register(Impactrating)
admin.site.register(Incidenteffect)
admin.site.register(Lossproperty)
admin.site.register(Malwaretype)
admin.site.register(Securitycompromise)
admin.site.register(Systemtype)
admin.site.register(Threatactortype)
admin.site.register(Discoverymethod)
admin.site.register(Lossduration)
