from django.core.management.base import BaseCommand
from shorturl.models import Link
import pyshorteners


class Command(BaseCommand):
    def __init__(self, text):
        self.text = text

    def handle(self, *args, **options):
        s = pyshorteners.Shortener()
        url = self.text
        surl = s.tinyurl.short(url)
        Link.objects.get_or_create(fullurl=self.text, newurl=surl, count=1)
        print(surl)
        return surl
