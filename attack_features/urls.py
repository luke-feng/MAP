from django.urls import path,re_path
# 导入 myapp 应用的 views 文件
from attack_features import views
from rest_framework.routers import DefaultRouter

app_name = 'attack_features'

router = DefaultRouter()

urlpatterns = [
    re_path(r'api/AttackFeatureRecordCreate/', views.AttackFeatureRecordCreate.as_view()),
    ]
