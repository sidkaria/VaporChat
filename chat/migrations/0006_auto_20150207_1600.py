# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_remove_chatuser_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatuser',
            name='confirm_code',
            field=models.CharField(max_length=32, default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chatuser',
            name='confirmed',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
    ]
