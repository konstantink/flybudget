# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.db.models import Sum
from django.views.generic import View

from rest_framework.response import Response
from rest_framework.views import APIView

import core.models as cm
import core.serializers as cs

# Create your views here.


class CategoryView(View):

    # @authenticate
    def get(self, request, *args, **kwargs):
        categories = cm.Category.objects.all()
        return JsonResponse(categories)


class EntryView(View):

    # @authenticate
    def get(self, request, *args, **kwargs):
        return JsonResponse({})


class ExpensesView(APIView):

    def get(self, request, format=None):
        entries = cm.Entry.objects.order_by('-date').all()[:100]
        data = cs.EntrySerializer(entries, many=True).data
        return Response(data=data)


class StatisticsView(APIView):

    def get(self, request, format=None):
        stats = {k: v for k, v in cm.Entry.objects.values('category__name').annotate(spent=Sum('total'))
                 .order_by('-spent').values_list('category__name', 'spent')}
        return JsonResponse(data=stats, safe=False)