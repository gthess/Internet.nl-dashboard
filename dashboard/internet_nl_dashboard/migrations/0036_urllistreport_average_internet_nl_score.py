# Generated by Django 2.2.2 on 2019-06-28 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internet_nl_dashboard', '0035_auto_20190624_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='urllistreport',
            name='average_internet_nl_score',
            field=models.FloatField(
                default=0, help_text='Internet.nl scores are retrieved in point. The calculation done for that is complex and subject to change over time. Therefore it is impossible to re-calculate that score here.Instead the score is stored as a given.'),
        ),
    ]
