# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0003_auto_20151001_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cornerstoneuserprofile',
            name='User_ID',
            field=models.IntegerField(),
        ),
    ]
