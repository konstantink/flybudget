# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.generic import View

import core.models as cm

# Create your views here.


class CategoryView(View):

    def get(self, response, *args, **kwargs):
        categories = cm.Category.objects.all()
        return JsonResponse(categories)
