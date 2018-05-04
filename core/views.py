# coding=UTF-8


__author__ = 'Konstantin Kolesnikov'


from django.http.response import HttpResponse
from django.views.generic import TemplateView


class DashboardView(TemplateView):

    def get(self, request, *args, **kwargs):
        return HttpResponse(request, status=200)
