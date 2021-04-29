"""SHINE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf.urls import url

import city_country.urls
import attack_information.urls
import measure.urls
import measure_type.urls
import organization.urls
import sector.urls
import application.urls
import attack_features.urls
from rest_framework import routers
import information_sharing.urls
import user_info.urls

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', TemplateView.as_view(template_name="index.html")),
    # url(r'^organization/select_citics/(?P<countryid>\d+)', views.select_citics),
    url(r'^chaining/', include('smart_selects.urls')),
    re_path(r'^sector/', include(sector.urls)),
    re_path(r'^application/', include(application.urls)),
    re_path(r'^city_country/', include(city_country.urls)),
    re_path(r'^organization/', include(organization.urls)),
    re_path(r'^attackinfo/', include(attack_information.urls)),
    re_path(r'^info_share/', include(information_sharing.urls)),
    re_path(r'^attackfeatures/', include(attack_features.urls)),
    re_path(r'^userinfo/', include(user_info.urls)),
    re_path(r'measures/', include(measure.urls)),
    re_path(r'measuretype/', include(measure_type.urls)),

    path("api/", include(router.urls)),
    path("api/auth", include("rest_framework.urls", namespace="rest_framework")),

    re_path(r'.*', TemplateView.as_view(template_name='index.html')),

]

