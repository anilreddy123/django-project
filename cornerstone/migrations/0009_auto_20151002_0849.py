# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0008_auto_20151002_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cornerstoneuserprofile',
            name='Manager_GUID',
        ),
        migrations.AlterField(
            model_name='cornerstoneuserprofile',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='cornerstone.CornerstoneUserProfile', null=True),
        ),
    ]
