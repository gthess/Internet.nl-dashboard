# Generated by Django 2.1.7 on 2019-03-18 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0053_url_do_not_find_subdomains'),
        ('internet_nl_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrlList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    blank=True, help_text='Name of the UrlList, for example name of the organization in it.', max_length=120, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='internet_nl_api_password',
            field=models.CharField(
                blank=True, help_text='New values will automatically be encrypted.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='urllist',
            name='account',
            field=models.ForeignKey(help_text='Who owns and manages this urllist.',
                                    on_delete=django.db.models.deletion.CASCADE, to='internet_nl_dashboard.Account'),
        ),
        migrations.AddField(
            model_name='urllist',
            name='urls',
            field=models.ManyToManyField(blank=True, related_name='urls_in_dashboard_list', to='organizations.Url'),
        ),
    ]
