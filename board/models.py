from django.db import models

from common.models import TimeStampedModel
from user.models import User


class Post(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    contents = models.TextField()
    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'post'


class PostComment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.TextField()
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'post_comment'
