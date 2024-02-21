from django.core.management import BaseCommand
import json

from catalog.models import Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data

    def handle(self, *args, **options):

        Category.objects.all().delete()

        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(Category(name=category['fields']['name'], about=category['fields']['about']))

        Category.objects.bulk_create(category_for_create)
