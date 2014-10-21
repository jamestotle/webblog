# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_blog_visit_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='visit_time',
            new_name='visit_count',
        ),
        migrations.AlterField(
            model_name='blog',
            name='context',
            field=models.TextField(default='无内容'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='blog',
            field=models.ForeignKey(to='blogs.Blog'),
        ),
    ]
