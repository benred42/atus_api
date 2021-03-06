"""atus_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'activities', views.ActivityViewSet)
router.register(r'respondents', views.RespondentsViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^respondents/(?P<respondent_id>\d+)/events', views.EventView.as_view(), name="event_list"),
    url(r'^respondents/(?P<respondent_id>\d+)/hhmembers', views.HouseholdMemberView.as_view(), name="hhmembers_list"),
]
