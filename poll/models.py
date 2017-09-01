#coding:utf8
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=30)
    pub_date = models.DateTimeField(verbose_name='发起时间')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.boolean = True
    was_published_recently.short_description = '是否最近一天发起?'

    def __unicode__(self): # python3是 __str__
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return self.choice_text