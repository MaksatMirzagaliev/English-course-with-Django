# Generated by Django 4.1.5 on 2023-02-23 05:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_sendmessageforteacher_alter_category_posted_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('first_name', models.CharField(blank=True, max_length=200)),
                ('middle_name', models.CharField(blank=True, max_length=200)),
                ('iin', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('password', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='posted_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 11, 22, 54, 29130)),
        ),
        migrations.AlterField(
            model_name='news',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 11, 22, 54, 95079)),
        ),
    ]
