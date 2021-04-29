from django.urls import path,re_path
# 导入 myapp 应用的 views 文件
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'measure_type'

router = DefaultRouter()

urlpatterns = [

    re_path(r'api/MeasuretypeList/', views.MeasuretypeList.as_view()),

]
