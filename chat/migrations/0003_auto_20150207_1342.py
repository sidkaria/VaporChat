# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20150207_1339'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='chatusers',
            new_name='ChatUser',
        ),
    ]
