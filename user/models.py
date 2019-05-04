from django.db import models

from common.models import TimeStampedModel


class User(TimeStampedModel):
    nickname = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    introduce = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'


class Creator(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    introduce = models.CharField(max_length=255)
    video_style = models.CharField(max_length=50)
    video_category = models.CharField(max_length=50)

    class Meta:
        db_table = 'creator'


class Editor(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    introduce = models.CharField(max_length=255)
    edit_style = models.CharField(max_length=50)
    edit_category = models.CharField(max_length=50)
    pay_type = models.CharField(max_length=50)

    class Meta:
      db_table = 'editor'
