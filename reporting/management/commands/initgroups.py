from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Creates groups for the the SALW project'

    def add_arguments(self, parser):
        parser.add_argument('new_groups', nargs='+', type=str)

    def handle(self, *args, **options):

        for new_group in options['new_groups']:
            new_group, created = Group.objects.get_or_create(name=new_group)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created {new_group}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Warning: {new_group} already exists, did not create'))