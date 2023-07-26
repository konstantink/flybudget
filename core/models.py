# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from datetime import datetime, date

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import ugettext_lazy as _

# Create your models here.


class ActiveManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        queryset = super(ActiveManager, self).get_queryset(*args, **kwargs)
        return queryset.filter(~models.Q(is_deleted=True))


class TimestampModel(models.Model):

    created_at = models.DateTimeField(_(u'Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_(u'Updated at'), auto_now=True)
    deleted_at = models.DateTimeField(_(u'Deleted at'), null=True)

    is_deleted = models.BooleanField(_('Is deleted?'), default=False)

    raw_objects = models.Manager()

    class Meta:
        app_label = 'core'
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at',)
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted_at = datetime.utcnow()
        self.is_deleted = True
        self.save()


class Category(TimestampModel):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(_(u'Category name'), max_length=64)
    user = models.ManyToManyField(User, related_name='categories')
    superset = models.BooleanField(_('Global category'), default=False)
    super_category = models.ForeignKey('self', null=True, blank=True, limit_choices_to={'superset': True, 'user': user},
                                       related_name='subcategories')
    # NOTE: Probably another relation is required to unite SuperCategory and user FinancialPlan
    fin_plan = models.ForeignKey('FinancialPlan', related_name='supersets')
    # is_public = models.BooleanField(_('Is public'), default=False)

    objects = ActiveManager()

    class Meta:
        # app_label = 'core'
        verbose_name_plural = _(u'Categories')

    def __str__(self):
        return u'<Category: uuid={} name={}>'.format(self.uuid, self.name)

    def __repr__(self):
        return u'<Category: uuid=%s name=%s>' % (self.uuid, self.name)

    def to_json(self):
        return {
            'uuid': self.uuid,
            'name': self.name
        }


class Item(TimestampModel):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(_(u'Item name'), max_length=128)

    objects = ActiveManager()

    def __str__(self):
        return u'<Item: uuid={} name={}>'.format(self.uuid, self.name)

    def __repr__(self):
        return u'<Item: uuid={} name={}>'.format(self.uuid, self.name)

    def to_json(self):
        return {
            'uuid': self.uuid,
            'name': self.name
        }


class Entry(TimestampModel):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    user = models.ForeignKey(User, related_name='entries')
    item = models.ForeignKey(Item, related_name='entries')
    category = models.ForeignKey(Category, related_name='entries')
    date = models.DateField(_(u'Date'), auto_now=False)
    price = models.FloatField(_(u'Price'))
    quantity = models.FloatField(_(u'Quantity'))
    total = models.FloatField(_(u'Total'))
    units = models.CharField(_(u'Units'), max_length=10)

    objects = ActiveManager()

    class Meta:
        verbose_name_plural = _(u'Entries')

    def __str__(self):
        return u'<Entry: user={} item={} category={}>'.format(self.user.username, self.item.name, self.category.name)

    def __repr__(self):
        return u'<Entry: user={} item={} category={}>'.format(self.user.username, self.item.name, self.category.name)


class FinancialPlan(TimestampModel):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    user = models.OneToOneField(User, related_name='plan')

    class Meta:
        verbose_name_plural = _(u'FinancialPlans')

    def __repr__(self):
        return u'<FinancialPlan: user={}>'.format(self.user.username)


class Wallet(TimestampModel):
    pass


class Card(models.Model):
    number = models.CharField(_('Card number'), max_length=16)

    class Meta:
        abstract = True


class DebitCard(Card, TimestampModel):
    pass


class CreditCard(Card, TimestampModel):
    pass



