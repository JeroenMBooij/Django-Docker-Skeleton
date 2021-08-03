from django.conf import settings
from django.core.management.base import BaseCommand
from src.apps.users.models import User
import os, logging

class Command(BaseCommand):

    def handle(self, *args, **options):

        if User.objects.count() == 0:
            try:
                if not User.objects.filter(email=os.getenv('ADMIN_EMAIL', 'admin@admin.admin')).first():
                    print("Creating default superuser with email and password")
                    User.objects.create_superuser(os.getenv('ADMIN_EMAIL', 'admin@admin.admin'), os.getenv('ADMIN_PASSWORD', 'admin'))
            except Exception as error:
                print(f'Found an error trying to create the superuser: {error}')

        else:
            print('Admin accounts can only be initialized if no Accounts exist')