# your_app/management/commands/create_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker  # You may need to install the 'Faker' library: pip install Faker

class Command(BaseCommand):
    help = 'Create sample data for your app'

    def handle(self, *args, **options):
        fake = Faker()

        # Your data creation logic here
        for _ in range(10):  # Create 10 sample users
            User.objects.create(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
            )

        self.stdout.write(self.style.SUCCESS('Sample data created successfully.'))
