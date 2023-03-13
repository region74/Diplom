from django.db import models


class Link(models.Model):
    fullurl = models.CharField()
    newurl = models.CharField()
    count = models.IntegerField(default=0)

# Create your models here.
