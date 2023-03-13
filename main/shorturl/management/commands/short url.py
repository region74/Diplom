from django.core.management.base import BaseCommand, CommandError
from shorturl.models import Question as Poll
import pyshorteners


class Command(BaseCommand):
    def handle(self, *args, **options):
        for poll_id in options['poll_ids']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))


# Создаём экземпляр класса Shortener
s = pyshorteners.Shortener()
# Пользователь вводит ссылку
url = input('Введите ссылку для сокращения: ')
# Сокращаем ссылку и выводим её
print(s.tinyurl.short(url))
