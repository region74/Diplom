from django.db import models




class TimeStamp(models.Model):
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Link(TimeStamp, models.Model):
    fullurl = models.CharField(max_length=500)
    newurl = models.CharField(max_length=500)
    count = models.IntegerField(default=0)

    # def test(self,*args,**kwargs):
    #     print(args)
    #     print(kwargs)
    #     print('hello')

    def __str__(self):
        return f'Полная сслыка: {self.fullurl} Коротка ссылка: {self.newurl} Дата создания: {TimeStamp.create} Обращений: {self.count}'

# Create your models here.
