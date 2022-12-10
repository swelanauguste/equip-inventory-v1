from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Owner


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            name = fake.name()
            Owner.objects.get_or_create(name=name)
            self.stdout.write(self.style.SUCCESS(f"{name}"))
