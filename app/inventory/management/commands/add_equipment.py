from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Category, Equipment, Owner


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            category = Category.objects.get(pk=randint(1, 3))
            serial_number = fake.ean(length=8)
            owner = Owner.objects.get(pk=randint(1, 10))
            date_received = fake.date()
            date_issued = fake.date()
            Equipment.objects.get_or_create(
                category=category,
                serial_number=serial_number,
                owner=owner,
                date_received=date_received,
                date_issued=date_issued,
            )
            self.stdout.write(self.style.SUCCESS(f"{serial_number}"))
