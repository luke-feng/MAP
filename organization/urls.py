from django.urls import path,re_path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'organization'

router = DefaultRouter()

urlpatterns = [
    re_path(r'api/org_list/', views.OrganizationList.as_view()),
]
