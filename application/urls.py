from django.urls import path,re_path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'application'

router = DefaultRouter()

urlpatterns = [
    re_path(r'api/add_application/', views.ApplicationList.as_view()),
]
