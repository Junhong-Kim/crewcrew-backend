from django.db import models

from common.models import TimeStampedModel
from user.models import Creator, Editor


class RecruitPost(TimeStampedModel):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    contents = models.TextField()
    pay_type = models.CharField(max_length=50)

    class Meta:
        db_table = 'recruit_post'


class RecruitQnA(TimeStampedModel):
    recruit_post = models.ForeignKey(RecruitPost, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    class Meta:
        db_table = 'recruit_qna'


class RecruitProcess(TimeStampedModel):
    recruit_post = models.ForeignKey(RecruitPost, on_delete=models.CASCADE)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    resume_title = models.CharField(max_length=100)
    resume_contents = models.TextField()
    resume_file = models.CharField(max_length=255)
    resume_confirm = models.BooleanField(default=False)
    resume_result = models.CharField(max_length=50)

    class Meta:
        db_table = 'recruit_process'
