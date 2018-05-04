# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-30 15:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('deleted_at', models.DateTimeField(verbose_name='Deleted at')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted?')),
                ('uuid', models.UUIDField(default=uuid.UUID('cb2e5016-55d2-4d10-8018-d8bf34a04457'), primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='Category name')),
                ('user', models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('deleted_at', models.DateTimeField(verbose_name='Deleted at')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted?')),
                ('number', models.CharField(max_length=16, verbose_name='Card number')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('raw_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='DebitCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('deleted_at', models.DateTimeField(verbose_name='Deleted at')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted?')),
                ('number', models.CharField(max_length=16, verbose_name='Card number')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('raw_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('deleted_at', models.DateTimeField(verbose_name='Deleted at')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted?')),
                ('uuid', models.UUIDField(default=uuid.UUID('2385fa8b-3b63-462d-a3d9-d0e6386af4db'), primary_key=True, serialize=False)),
                ('units', models.CharField(max_length=10, verbose_name='Units')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='core.Category')),
            ],
            options={
                'verbose_name_plural': 'Entries',
            },
            managers=[
                ('raw_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('deleted_at', models.DateTimeField(verbose_name='Deleted at')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted?')),
                ('uuid', models.UUIDField(default=uuid.UUID('d39d19be-5076-4070-848d-e3d5ab51c27a'), primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='Item name')),
            ],
            options={
                'abstract': False,
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
            },
            managers=[
                ('raw_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('deleted_at', models.DateTimeField(verbose_name='Deleted at')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is deleted?')),
            ],
            options={
                'abstract': False,
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
            },
            managers=[
                ('raw_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='core.Item'),
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL),
        ),
    ]
