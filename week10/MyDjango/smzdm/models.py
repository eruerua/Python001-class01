from django.db import models

# Create your models here.
class T1(models.Model):
    author = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000)
    sentiment = models.FloatField()

    # 元数据，不属于任何一个字段的数据
    class Meta:
        managed = False
        db_table = 'smzdm_senti'