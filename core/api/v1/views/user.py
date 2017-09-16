# coding=utf-8


from functools import wraps

from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.views.generic import View

__author__ = 'kkolesnikov'


def extract_params(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        self, request = args[:2]
        return f(*args, **kwargs)


class UserRegisterView(View):

    @extract_params
    def post(self, request, *args, **kwargs):


class UserSigninView(View):

    def post(self, request, *args, **kwargs):
        return JsonResponse()