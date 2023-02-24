# Generated by Django 4.1.5 on 2023-02-20 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_teacher_experience_alter_category_posted_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='location_cart',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='posted_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 23, 36, 15, 774702)),
        ),
        migrations.AlterField(
            model_name='news',
            name='posted_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 20, 23, 36, 15, 870769)),
        ),
    ]