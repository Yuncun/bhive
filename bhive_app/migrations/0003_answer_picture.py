# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bhive_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('bhive_app', '0002_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='picture',
            field=models.ImageField(upload_to=bhive_app.models.upload_pic_to, verbose_name=b'Picture', blank=True),
            preserve_default=True,
        ),
    ]
