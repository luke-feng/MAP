from django.urls import path,re_path
# 导入 myapp 应用的 views 文件
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'user_info'

router = DefaultRouter()

urlpatterns = [
    re_path(r'api/UserDetail/(?P<pk>[a-zA-Z0-9]+)$', views.UserDetail.as_view()),
    re_path(r'api/UserList/', views.UserList.as_view()),
    re_path(r'api/UserCreate/', views.UserCreate.as_view()),

    ]
