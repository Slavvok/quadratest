from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from newapi import views
from django.conf import settings

urlpatterns = [
    url(r'^upload/$', views.uploadText.as_view(), name="uploadtext"),
    url(r'^get/$', views.getText.as_view(), name="gettext"),
]
