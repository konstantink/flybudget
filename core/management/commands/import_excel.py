# coding=UTF-8


import sys
import pandas as pd
import uuid

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db.models import Count, Sum
from django.utils.termcolors import colorize

from core.models import Category, Item, Entry


__author__ = 'Konstantin Kolesnikov'


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', action='store', type=str, required=True)

    def handle(self, *args, **options):
        filepath = options['file']
        try:
            excel = pd.ExcelFile(filepath)
        except FileNotFoundError:
            self.stderr.write('ERROR: Can\'t find file')
            sys.exit(1)

        df = None
        existing_categories = set(Category.objects.values_list('name', flat=True))
        existing_items = set(Item.raw_objects.values_list('name', flat=True))

        # Skip the first sheet as it is category dictionary
        for sheet in excel.sheet_names[1:]:
            self.stdout.write('=> Reading sheet \'{}\''.format(sheet))
            if df is None:
                df = excel.parse(sheet, usecols=3)
                continue
            df = pd.concat([df, excel.parse(sheet, usecols=3)])

        categories_from_file = self.get_set_of_values(df, 'Category')
        new_categories = categories_from_file - existing_categories
        items_from_file = self.get_set_of_values(df, 'Item')
        new_items = items_from_file - existing_items

        self.stdout.write('==> Found {} unique values for \'Category\', {} {} new'
                          .format(len(categories_from_file), len(new_categories),
                                  'are' if len(new_categories) > 1 else 'is'))
        self.stdout.write('==> Found {} unique values for \'Item\', {} {} new'
                          .format(len(items_from_file), len(new_items), 'are' if len(new_items) > 1 else 'is'))

        self.create_categories(new_categories)
        self.create_items(new_items)
        self.create_entries(df)

        query = Entry.objects.values('category__name').annotate(item_cnt=Count('item'), total_sum=Sum('total'))\
            .values_list('category__name', 'item_cnt', 'total_sum').order_by('category__name')
        self.stdout.write(colorize('Summary:', fg='blue', opts=('underscore', 'bold')))
        for row in query:
            row = (row[0], row[1], colorize('£{:.02f}'.format(row[2]), fg='red', opts=('bold',)))
            self.stdout.write('==> Created {} for {} total sum {}'.format(*row))

        sys.exit(0)

    def create_categories(self, categories):
        user = User.objects.get(pk=1)
        category_objs = [Category(uuid=uuid.uuid4(), name=category) for category in categories]
        created_objs = Category.objects.bulk_create(category_objs)
        list(map(lambda x: x.user.add(user.pk), created_objs))
        for obj in created_objs[:10]:
            self.stdout.write('===> Created {}'.format(obj))
        else:
            if len(created_objs) > 10:
                self.stdout.write('===> ... and {} more objects'.format(len(created_objs)-10))
        return created_objs

    def create_items(self, items):
        item_objs = [Item(uuid=uuid.uuid4(), name=item) for item in items]
        created_objs = Item.objects.bulk_create(item_objs)
        for obj in created_objs[:10]:
            self.stdout.write('===> Created {}'.format(obj))
        else:
            if len(created_objs) > 10:
                self.stdout.write('===> ... and {} more objects'.format(len(created_objs) - 10))
        return created_objs

    def create_entries(self, df):
        entry_objs = []
        user = User.objects.get(pk=1)
        for idx, data in df.iterrows():
            category = Category.objects.get(name=data['Category'])
            item = Item.objects.get(name=data['Item'])
            entry_objs.append(Entry(uuid=uuid.uuid4(), user=user, category=category, item=item,
                                    date=data['Date'].date(), price=data['Expenses'], quantity=1.,
                                    total=data['Expenses']))

        created_objs = Entry.objects.bulk_create(entry_objs)
        for obj in created_objs[:10]:
            self.stdout.write('===> Created {}'.format(obj))
        else:
            if len(created_objs) > 10:
                self.stdout.write('===> ... and {} more objects'.format(len(created_objs) - 10))

    def get_set_of_values(self, df, column):
        """
        :param df: DataFrame from which to extract values
        :param column: Name of the column to collect unique items
        :return: Set of unique values from the given column
        """
        return set(df[df[column].notnull()][column])
