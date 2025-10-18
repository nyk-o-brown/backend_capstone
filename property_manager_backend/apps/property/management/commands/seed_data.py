from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.property.models import Property
from faker import Faker
import random

fake = Faker()
User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with users and properties'

    def handle(self, *args, **kwargs):
        # Create users
        for _ in range(5):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123',
                phone=fake.phone_number()
            )
            self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))

            # Create properties for each user
            for _ in range(random.randint(1, 3)):
                prop = Property.objects.create(
                    owner=user,
                    name=fake.company(),
                    location=fake.address(),
                )
                self.stdout.write(self.style.SUCCESS(f'  ↳ Property: {prop.name}'))
