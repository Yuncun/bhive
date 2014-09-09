from django.db import models


class Question(models.Model):
    user_id = models.CharField(max_length=36)
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=25)
    votes = models.IntegerField(default=0)