#coding:utf-8

from django.db import models
from django.utils import timezone

class Blog(models.Model):
  tag = models.CharField(max_length=10,default=u'未分类')
  title = models.CharField(max_length = 30,default=u'无标题')
  context = models.TextField(default='无内容')
  pub_date = models.DateTimeField('date published')
  visit_count = models.IntegerField(default=0)
  def __str__(self):
    return self.title
  def __unicode__(self):
    return self.title
  def was_publish_recently(self):
    return self.pub_date>=timezone.now()-datetime.timedelta(days=5)

class Vote(models.Model):
  blog = models.ForeignKey(Blog)
  thumb_up = models.IntegerField(default = 0)
  thumb_down = models.IntegerField(default = 0)
