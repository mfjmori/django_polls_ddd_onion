import datetime
from django.utils import timezone
from django.db import models


class Question(models.Model):
    id = models.UUIDField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    id = models.UUIDField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
