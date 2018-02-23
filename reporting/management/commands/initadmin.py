import os
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.management.commands.createsuperuser import get_user_model


class Command(BaseCommand):
    help = 'Initiates a superuser account based on environment variables'

    def handle(self, *args, **options):
        try:
            get_user_model()._default_manager.db_manager('default').create_superuser(
                username=os.environ.get('DJANGO_SU_NAME'),
                email=os.environ.get('DJANGO_SU_EMAIL'),
                password=os.environ.get('DJANGO_SU_PASSWORD')
                )

            self.stdout.write(self.style.SUCCESS('Successfully created default superuser'))

        except KeyError:
            raise CommandError('One or more environment variables are not set')
