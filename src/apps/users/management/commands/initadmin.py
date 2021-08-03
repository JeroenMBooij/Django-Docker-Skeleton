from django.conf import settings
from django.core.management.base import BaseCommand
from src.apps.users.models import User
import os, logging

class Command(BaseCommand):

    def handle(self, *args, **options):
        logger = logging.getLogger('')

        if User.objects.count() == 0:
            try:
                if not User.objects.filter(username="admin").first():
                    logger.info("Creating default superuser with user and password: admin")
                    User.objects.create_superuser(os.getenv('ADMIN_EMAIL', 'admin@admin.admin'), os.getenv('ADMIN_PASSWORD', 'admin'))
            except Exception as error:
                logger.info(f'Found an error trying to create the superuser: {error}')

        else:
            logger.info('Admin accounts can only be initialized if no Accounts exist')