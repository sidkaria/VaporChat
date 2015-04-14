# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20150207_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatuser',
            name='password',
            field=models.CharField(max_length=32, default=datetime.datetime(2015, 2, 8, 17, 28, 43, 876724, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
