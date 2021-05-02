from django.urls import path,re_path
from attack_features import views
from rest_framework.routers import DefaultRouter

app_name = 'attack_features'

router = DefaultRouter()

urlpatterns = [
    re_path(r'api/AttackFeatureRecordCreate/', views.AttackFeatureRecordCreate.as_view()),
    ]
