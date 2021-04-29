from django.urls import path,re_path
# 导入 myapp 应用的 views 文件
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'application'

router = DefaultRouter()

urlpatterns = [
    re_path(r'api/add_application/', views.ApplicationList.as_view()),
]
