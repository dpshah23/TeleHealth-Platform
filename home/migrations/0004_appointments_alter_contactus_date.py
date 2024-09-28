# Generated by Django 5.0.6 on 2024-09-28 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contactus_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_email', models.CharField(max_length=200)),
                ('p_email', models.CharField(default=None, max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('specialization', models.CharField(max_length=100)),
                ('payment', models.CharField(max_length=10)),
                ('vc_link', models.TextField(default=None)),
                ('completed', models.BooleanField(default=False)),
                ('doc_paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='contactus',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 28, 9, 57, 30, 50427, tzinfo=datetime.timezone.utc)),
        ),
    ]
