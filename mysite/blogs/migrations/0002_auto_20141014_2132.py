# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thumb_up', models.IntegerField(default=0)),
                ('thumb_down', models.IntegerField(default=0)),
                ('blog', models.ForeignKey(to='blogs.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.CharField(default='\u672a\u5206\u7c7b', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'date published'),
        ),
    ]
