# Generated by Django 4.0.1 on 2024-09-28 05:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 28, 5, 30, 20, 214347, tzinfo=utc)),
        ),
    ]
