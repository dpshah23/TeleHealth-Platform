# Generated by Django 4.0.1 on 2024-09-29 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='joined',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.CharField(max_length=255)),
                ('doctor', models.CharField(max_length=200)),
                ('room', models.CharField(max_length=200)),
            ],
        ),
    ]
# Generated by Django 5.0.6 on 2024-09-29 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chatapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='joined',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.CharField(max_length=255)),
                ('doctor', models.CharField(max_length=200)),
                ('room', models.CharField(max_length=200)),
            ],
        ),
    ]
