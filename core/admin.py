# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

import core.models as models

# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Item)
admin.site.register(models.Entry)