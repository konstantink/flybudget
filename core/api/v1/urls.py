# coding=utf-8

from django.conf.urls import url

from views import main, user

__author__ = 'kkolesnikov'


urlpatterns = (
    url(r'^categories', main.CategoryView.as_view()),
)