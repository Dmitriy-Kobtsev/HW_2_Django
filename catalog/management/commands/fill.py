from django.core.management import BaseCommand
import json

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('product_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        category_data = []
        for item in data:
            if item['model'] == 'catalog.category':
                category_data.append(item)

        return category_data

    @staticmethod
    def json_read_products():
        with open('product_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        product_data = []
        for item in data:
            if item['model'] == 'catalog.product':
                product_data.append(item)

        return product_data

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        category_for_create = []
        product_for_create = []

        for category in Command.json_read_categories():
            print(f' pk = {category["pk"]}')
            category_for_create.append(Category(id=category['pk'],
                                                name=category['fields']['name'],
                                                about=category['fields']['about']))

        Category.objects.bulk_create(category_for_create)


        for product in Command.json_read_products():
            product_for_create.append(Product(product_name=product['fields']['product_name'],
                                              product_about=product['fields']['product_about'],
                                              product_category_id=product['fields']['product_category'],
                                              product_price=product['fields']['product_price']))

        Product.objects.bulk_create(product_for_create)
