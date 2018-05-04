# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.serializers import ModelSerializer

import core.models as cm


class CategorySerializer(ModelSerializer):

    class Meta:
        model = cm.Category


class ItemSerializer(ModelSerializer):

    class Meta:
        model = cm.Item


class EntrySerializer(ModelSerializer):

    # fields = __all__

    class Meta:
        fields = '__all__'
        model = cm.Entry
        depth = 1
