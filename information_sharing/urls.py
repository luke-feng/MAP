from django.urls import path,re_path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'information_sharing'

router = DefaultRouter()

urlpatterns = [
    re_path(r'api/AssettypeList/', views.AssettypeList.as_view()),
    re_path(r'api/AttackerinfrastructureList/', views.AttackerinfrastructureList.as_view()),
    re_path(r'api/AttackertoolList/', views.AttackertoolList.as_view()),
    re_path(r'api/ImpactratingList/', views.ImpactratingList.as_view()),
    re_path(r'api/IncidentcategoryList/', views.IncidentcategoryList.as_view()),
    re_path(r'api/IncidenteffectList/', views.IncidenteffectList.as_view()),
    re_path(r'api/LosspropertyList/', views.LosspropertyList.as_view()),
    re_path(r'api/MalwaretypeList/', views.MalwaretypeList.as_view()),
    re_path(r'api/SecuritycompromiseList/', views.SecuritycompromiseList.as_view()),
    re_path(r'api/SystemtypeList/', views.SystemtypeList.as_view()),
    re_path(r'api/ThreatactortypeList/', views.ThreatactortypeList.as_view()),
    re_path(r'api/DiscoverymethodList/', views.DiscoverymethodList.as_view()),
    re_path(r'api/LossdurationList/', views.LossdurationList.as_view())
]

