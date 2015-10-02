# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0007_cornerstoneuserprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cornerstoneuserprofile',
            name='Manager_ID',
        ),
        migrations.AddField(
            model_name='cornerstoneuserprofile',
            name='Manager_GUID',
            field=models.UUIDField(null=True, blank=True),
        ),
    ]
