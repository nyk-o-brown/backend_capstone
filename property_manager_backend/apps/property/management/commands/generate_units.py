from django.core.management.base import BaseCommand
from faker import Faker
import random
from apps.property.models import Property, Unit
from django.contrib.auth import get_user_model

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Generate mock units for existing properties'

    def handle(self, *args, **kwargs):
        properties = Property.objects.all()
        users = list(User.objects.all())

        if not properties:
            self.stdout.write(self.style.ERROR("No properties found. Create some first."))
            return

        for prop in properties:
            for _ in range(random.randint(2, 5)):  # 2–5 units per property
                unit = Unit.objects.create(
                    property=prop,
                    name=fake.number() + " Unit",
                    floor=str(random.randint(1, 10)),
                    tenant=random.choice(users) if random.random() < 0.7 else None
                )
                self.stdout.write(self.style.SUCCESS(f"Created unit: {unit.name} for {prop.name}"))
