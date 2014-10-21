# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20141014_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='visit_time',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
