# Generated by Django 2.2.3 on 2020-09-24 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20200924_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='endTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='startTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 24, 13, 14, 19, 113550)),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 24, 13, 14, 19, 114545)),
        ),
    ]
