# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20141014_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='context',
            field=models.TextField(default=b'\xe6\x97\xa0\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='\u65e0\u6807\u9898', max_length=30),
        ),
    ]
