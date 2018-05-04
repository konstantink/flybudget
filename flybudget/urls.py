"""flybudget URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

import json

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import generic
from rest_framework.schemas import get_schema_view

from core.views import DashboardView


def index(request, *args, **kwargs):
    f = open('web/app/fake/testData.json', 'r')#, encoding='utf-8')
    data = json.loads(''.join(f.readlines()))
    return render(request, '../frontend/index.html', context={'initialData': data['data']})


def data(request, *args, **kwargs):
    if request.method == 'GET':
        f = open('web/app/fake/testData.json', 'r', encoding='utf-8')
        return JsonResponse(json.loads(''.join(f.readlines())), encoder=json.JSONEncoder)


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # url(r'^$', generic.RedirectView.as_view(url='/dashboard/', permanent=False)),

    url(r'^dashboard', DashboardView.as_view()),

    # url(r'^login', login),

    # url(r'^$', generic.RedirectView.as_view(
    #      url='/api/', permanent=False)),
    # url(r'^api/$', get_schema_view()),

    url(r'^api/v1/', include('core.api.v1.urls')),

    url(r'^$', index),
    # url(r'^data', data),
]
