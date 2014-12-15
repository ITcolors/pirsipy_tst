# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0003_auto_20141203_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_id',
            field=models.CharField(default=uuid.uuid4, unique=True, max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
