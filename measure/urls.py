from django.urls import path,re_path
from measure import views
from rest_framework.routers import DefaultRouter

app_name = 'measure'

router = DefaultRouter()

urlpatterns = [
    re_path(r'api/MeasureRecordCreate/', views.MeasureRecordCreate.as_view()),
    re_path(r'api/MeasureRecordList/(?P<userid>[a-zA-Z0-9]+)/(?P<incident_category>[0-9]+)$', views.MeasureRecordList.as_view()),
    re_path(r'api/MeasureRecordListByUser/(?P<userid>[a-zA-Z0-9]+)$', views.MeasureRecordListByUser.as_view())
]
