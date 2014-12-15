# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0002_auto_20141202_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=b'/home/alex/Dev/pirsipy-task/pirsiblog/pirsiblog_dev/pirsiblog_proj/posting/media/img', blank=True),
            preserve_default=True,
        ),
    ]
