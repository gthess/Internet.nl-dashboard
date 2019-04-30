# Generated by Django 2.2 on 2019-04-30 10:21

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('internet_nl_dashboard', '0024_auto_20190429_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urllist',
            name='scheduled_next_scan',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 10, 21, 57, 14534, tzinfo=utc),
                                       help_text='An indication at what moment the scan will be started. The scan can take a while, thus this does not tell you when a scan will be finished. All dates in the past will be scanned and updated.'),
        ),
    ]
