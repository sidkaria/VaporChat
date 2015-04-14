# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20150207_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatuser',
            name='age',
        ),
    ]
