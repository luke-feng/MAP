from django.urls import path,re_path
from attack_information import views
from rest_framework.routers import DefaultRouter

app_name = 'attack_information'

router = DefaultRouter()

urlpatterns = [
    re_path(r'api/MonthlyLossSum/(?P<group>\w+)/(?P<id>\w+)$', views.MonthlyLossSum.as_view()),
    re_path(r'api/MonthlyAttackTimes/(?P<orgid>\w+)$', views.MonthlyAttackTimes.as_view()),
    re_path(r'api/AttackTimesBySector/', views.AttackTimesBySector.as_view()),
    re_path(r'api/AttackTypeLossSum/(?P<group>\w+)/(?P<id>\w+)$', views.AttackTypeLossSum.as_view()),
    re_path(r'api/YearlyLossSumBySector/', views.YearlyLossSumBySector.as_view()),
    re_path(r'api/YearlyLossSumByLossCate/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyLossSumByLossCate.as_view()),

    re_path(r'api/MonthlyImpactRating/(?P<group>\w+)/(?P<id>\w+)$', views.MonthlyImpactRating.as_view()),

    re_path(r'api/overviewIncidentCate/(?P<group>\w+)/(?P<id>\w+)$', views.IncidentCateList.as_view()),

    re_path(r'api/MonthlyIncidentCateList/(?P<group>\w+)/(?P<orgid>\w+)$', views.MonthlyIncidentCateList.as_view()),


            # http://127.0.0.1:8000/attackinfo/api/IncidentEffectTimes/sector/sector_id

            # http://127.0.0.1:8000/attackinfo/api/IncidentEffectTimes/org/orgnization_id
    re_path(r'api/YearlyIncidentEffectTimes/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyIncidentEffectTimes.as_view()),

    re_path(r'api/MonthlySecurityCompromise/(?P<group>\w+)/(?P<id>\w+)$', views.MonthlySecurityCompromise.as_view()),

    re_path(r'api/YearlyTopAttackerInfrastructure/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyTopAttackerInfrastructure.as_view()),

    re_path(r'api/YearlyTopThreatActorType/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyTopThreatActorType.as_view()),

    re_path(r'api/YearlyTopAttackerTool/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyTopAttackerTool.as_view()),

    re_path(r'api/YearlyTopMalwareType/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyTopMalwareType.as_view()),

    re_path(r'api/YearlyTopSystemType/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyTopSystemType.as_view()),

    re_path(r'api/YearlyTopLossProperty/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyTopLossProperty.as_view()),

    re_path(r'api/YearlyLossDuration/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyLossDuration.as_view()),

    re_path(r'api/YearlyTopIpWatchlist/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyTopIpWatchlist.as_view()),

    re_path(r'api/YearlyTopMaliciousEmailWatchlist/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyTopMaliciousEmailWatchlist.as_view()),

    re_path(r'api/YearlyTopFileHashWatchlist/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyTopFileHashWatchlist.as_view()),

    re_path(r'api/YearlyTopDomainWatchlist/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyTopDomainWatchlist.as_view()),

    re_path(r'api/YearlyTopURLWatchlist/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyTopURLWatchlist.as_view()),

    re_path(r'api/YearlyTopAssetType/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyTopAssetType.as_view()),

    re_path(r'api/YearlyDiscoveryMethod/(?P<group>\w+)/(?P<id>\w+)$', views.YearlyDiscoveryMethod.as_view()),

    re_path(r'api/MonthlyLossDuration/(?P<group>\w+)/(?P<id>\w+)$', views.MonthlyLossDuration.as_view()),

    re_path(r'api/AttackInformationDetail/(?P<pk>\w+)$', views.AttackInformationDetail.as_view()),
    re_path(r'api/AttackInformationRecordCreate/', views.AttackInformationRecordCreate.as_view())


]
