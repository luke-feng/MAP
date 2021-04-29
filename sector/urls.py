from django.urls import path,re_path
# 导入 myapp 应用的 views 文件
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'sector'

router = DefaultRouter()

urlpatterns = [
    re_path(r'add_sector$', views.add_sector),
    re_path(r'show_sectors$', views.show_sectors),
    re_path(r'api/show_sector/', views.SectorListAPIView.as_view()),
    re_path(r'api/sector_detail/(?P<pk>[0-9]+)$', views.SectorDetail.as_view()),
    re_path(r'api/sector_list/', views.SectorList.as_view()),
]
