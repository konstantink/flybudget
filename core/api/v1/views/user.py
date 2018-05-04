# coding=utf-8


import json

from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

__author__ = 'kkolesnikov'


class UserSignupView(APIView):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        return JsonResponse(data, json.JSONEncoder)


class UserSigninView(LoginView):

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        return JsonResponse()