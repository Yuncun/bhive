from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    user_id = models.CharField(max_length=36)
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'Question #{}'.format(self.pk)


def upload_pic_to(instance, filename):
    import os
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'pictures/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )

class Answer(models.Model):
    picture = models.ImageField(("Picture"), upload_to=upload_pic_to, blank=True)
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=25)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return u'Answer to question {} ({} votes)'.format(self.question_id, self.votes)


class Vote(models.Model):
    answer = models.ForeignKey(Answer)
    user = models.ForeignKey(User)
