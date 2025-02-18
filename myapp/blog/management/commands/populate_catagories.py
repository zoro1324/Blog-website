from blog.models import Catagory
from typing import Any
from django.core.management.base import BaseCommand
class Command(BaseCommand):

    def handle(self, *args, **options):
        Catagory.objects.all().delete()
        catagories = ["Anime","Movies","Games","Sports","Technology"]
        for catagory in catagories:
            Catagory.objects.create(catagory_name = catagory)

        self.stdout.write(self.style.SUCCESS("Successfully insereted."))