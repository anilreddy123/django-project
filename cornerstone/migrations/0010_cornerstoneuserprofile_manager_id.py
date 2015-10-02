# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0009_auto_20151002_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='cornerstoneuserprofile',
            name='Manager_ID',
            field=models.IntegerField(null=True),
        ),
    ]
