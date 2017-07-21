# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import ugettext_lazy as _

# Create your models here.


class TimestampModel(models.Model):

    created_at = models.DateTimeField(_(u'Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_(u'Updated at'), auto_now=True)
    deleted_at = models.DateTimeField(_(u'Deleted at'))

    class Meta:
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted_at = datetime.utcnow()


class Category(TimestampModel):

    uuid = models.UUIDField(unique=True, default=uuid.uuid4())
    name = models.CharField(_(u'Category name'), max_length=64)
    user = models.ManyToManyField(User, related_name='categories')

    class Meta:
        verbose_name_plural = _(u'Categories')


class Item(TimestampModel):

    uuid = models.UUIDField(unique=True, default=uuid.uuid4())
    name = models.CharField(_(u'Item name'), max_length=128)


class Entry(TimestampModel):

    uuid = models.UUIDField(unique=True, default=uuid.uuid4())
    user = models.ForeignKey(User, related_name='entries')
    item = models.ForeignKey(Item, related_name='entries')
    category = models.ForeignKey(Category, related_name='entries')
