# coding=utf-8


from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.views.generic import View

__author__ = 'kkolesnikov'


class UserSigninView(View):

    def post(self, request, *args, **kwargs):
        return JsonResponse()