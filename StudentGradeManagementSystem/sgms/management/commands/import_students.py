import csv
from django.core.management.base import BaseCommand
from sgms.models import Student
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Import students from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = User.objects.create_user(
                    username=row['email'],  # Or any other unique identifier
                    email=row['email'],
                    password='default_password'  # Set a default password
                )
                Student.objects.create(
                    user=user,
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                )
                self.stdout.write(self.style.SUCCESS(f"Successfully imported {row['first_name']} {row['last_name']}"))
