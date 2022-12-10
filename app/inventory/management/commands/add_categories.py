from django.core.management.base import BaseCommand

from ...models import Category

CATEGORY_LIST = [
    "computer",
    "printer",
    "scanner",
]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for _ in CATEGORY_LIST:
            category = _.lower()
            Category.objects.get_or_create(category=category)
            self.stdout.write(self.style.SUCCESS(f"{category}"))
