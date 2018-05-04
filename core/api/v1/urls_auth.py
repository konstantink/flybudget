# coding=UTF-8


from django.conf.urls import url

from core.api.v1.views import user


__author__ = 'Konstantin Kolesnikov'


urlpatterns = (
    url(r'^signup', user.UserSignupView.as_view(), name='user_signup'),
    url(r'^signin', user.UserSigninView.as_view(), name='user_signin',),
)
