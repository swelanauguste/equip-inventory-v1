from random import randint

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Category, Equipment, Owner


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(250):
            category = Category.objects.get(pk=randint(1, 3))
            serial_number = fake.ean(length=8)
            make_model = fake.text(max_nb_chars=20)
            owner = Owner.objects.get(pk=randint(1, 10))
            date_received = fake.date()
            date_issued = fake.date()
            Equipment.objects.get_or_create(
                category=category,
                serial_number=serial_number,
                make_model=make_model,
                owner=owner,
                date_received=date_received,
                date_issued=date_issued,
            )
            self.stdout.write(self.style.SUCCESS(f"{serial_number}"))
