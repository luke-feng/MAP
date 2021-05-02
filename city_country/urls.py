from django.urls import path,re_path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'city_country'

router = DefaultRouter()

urlpatterns = [
    re_path(r'api/country_list/', views.CountryList.as_view()),
    re_path(r'api/city_detail/(?P<pk>[0-9]+)$', views.CityDetail.as_view()),
    re_path(r'api/city_list/', views.CityList.as_view()),
]
