from django.urls import path,re_path
# 导入 myapp 应用的 views 文件
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'organization'

router = DefaultRouter()
# router.register(r'sectorlist', views.SectorListAPIView )

urlpatterns = [
    # re_path(r'add_sector$', views.add_sector),
    # re_path(r'show_sectors$', views.show_sectors),
    # path('<int:pk>/', views.SectorDetail.as_view(), name='list')
    # path('api/country_list/', views.OrganizationList.as_view()),
    # re_path(r'api/city_detail/(?P<pk>[0-9]+)$', views.CityDetail.as_view()),
    re_path(r'api/org_list/', views.OrganizationList.as_view()),
]
