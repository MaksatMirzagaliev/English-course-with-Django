# Generated by Django 4.1.5 on 2023-02-20 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_posted_date_alter_news_posted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='logo',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AlterField(
            model_name='category',
            name='posted_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 12, 53, 44, 852848)),
        ),
        migrations.AlterField(
            model_name='news',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 12, 53, 44, 881018)),
        ),
    ]