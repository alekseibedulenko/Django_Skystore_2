import json

from django.core.management import BaseCommand

from catalog.models import Product, Category, Contact
from skystore.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Заполнение БД фикстурами'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Contact.objects.all().delete()

        with open(BASE_DIR / 'catalog/fixtures/category.json', encoding='cp1251') as fp:
            category_data = json.load(fp)
            for item in category_data:
                Category.objects.create(
                    pk=item['pk'],
                    name=item["fields"]["name"],
                    description=item["fields"]["description"]
                )
            with open(BASE_DIR / 'catalog/fixtures/product.json', encoding='cp1251') as fp:
                product_data = json.load(fp)
                for item in product_data:
                    category_pk = item["fields"]["category"]
                    category = Category.objects.get(pk=category_pk)
                    Product.objects.create(
                        pk=item['pk'],
                        name=item["fields"]["name"],
                        description=item["fields"]["description"],
                        preview_description=item["fields"]["preview_description"],
                        image=item["fields"]["image"],
                        category=category,
                        price=item["fields"]["price"],
                        created_at=item["fields"]["created_at"],
                        lost_modified=item["fields"]["lost_modified"],
                    )
            with open(BASE_DIR / 'catalog/fixtures/contact.json', encoding='cp1251') as fp:
                contact_data = json.load(fp)
                for item in contact_data:
                    Contact.objects.create(
                        pk=item['pk'],
                        country=item["fields"]["country"],
                        inn=item["fields"]["inn"],
                        address=item["fields"]["address"])
