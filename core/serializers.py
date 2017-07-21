# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.serializers import ModelSerializer

import models


class CategorySerializer(ModelSerializer):

    class Meta:
        model = models.Category


class ItemSerializer(ModelSerializer):

    class Meta:
        model = models.Item


class EntrySerializer(ModelSerializer):

    class Meta:
        model = models.Entry
