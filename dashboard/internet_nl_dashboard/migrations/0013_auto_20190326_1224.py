# Generated by Django 2.1.7 on 2019-03-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internet_nl_dashboard', '0012_account_can_connect_to_internet_nl_api'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='internet_nl_api_password',
            field=models.BinaryField(blank=True, editable=True,
                                     help_text='New values will automatically be encrypted.', null=True),
        ),
    ]
