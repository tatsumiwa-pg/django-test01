from django.db import models

class Test01(models.Model):
  class Meta:
      db_table = 't_memo' # memoテーブル
      verbose_name_plural = 't_memo'
  memo_id = models.IntegerField(verbose_name='memo_id', name='memo_id', primary_key=True, null=False, blank=True)
  memo_title = models.CharField(verbose_name='memo_title', name='memo_title', max_length=128, null=True, blank=True)
  contents = models.TextField(verbose_name='contents', name='contents', max_length=516, null=True, blank=True)
  created_at = models.DateTimeField(verbose_name='registered_datetime', name='register_dttm', max_length=14, null=False, auto_now=True)
  updated_at = models.DateTimeField(verbose_name='lastupdate_datetime', name='lastupdate_dttm', max_length=14, null=False, auto_now_add=True)
  