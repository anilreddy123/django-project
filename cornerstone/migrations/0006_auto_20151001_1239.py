# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0005_auto_20151001_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cornerstoneuserprofile',
            name='parent',
        ),
        migrations.DeleteModel(
            name='CornerstoneUserProfile',
        ),
    ]
