# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0002_auto_20151001_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cornerstoneuserprofile',
            name='Manager_ID',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
