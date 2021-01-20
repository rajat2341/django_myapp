from django.core.management import BaseCommand

from authentication.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        queryset = User.objects.filter(username="root")
        if not queryset:
            User.objects.create_superuser(username='root', email='root@root.com', password='root')
