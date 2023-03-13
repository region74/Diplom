from django.db import models


class Link(models.Model):
    fullurl = models.CharField(max_length=500)
    newurl = models.CharField(max_length=500)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'Полная сслыка: {self.fullurl} Коротка ссылка: {self.newurl} Обращений: {self.count}'

# Create your models here.
