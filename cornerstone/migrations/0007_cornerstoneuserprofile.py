# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0006_auto_20151001_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='CornerstoneUserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('GUID', models.UUIDField()),
                ('User_ID', models.IntegerField()),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Manager_ID', models.IntegerField(null=True, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, to='cornerstone.CornerstoneUserProfile', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
