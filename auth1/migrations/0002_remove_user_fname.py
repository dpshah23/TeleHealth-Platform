# Generated by Django 5.0.6 on 2024-09-29 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fname',
        ),
    ]