# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0004_post_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.CharField(default=uuid.uuid4, unique=True, max_length=50, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
