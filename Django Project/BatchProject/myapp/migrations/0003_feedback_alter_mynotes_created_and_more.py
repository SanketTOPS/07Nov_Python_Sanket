# Generated by Django 4.1.4 on 2023-02-08 06:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_mynotes_alter_usersignup_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 8, 11, 46, 30, 386035))),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='mynotes',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 8, 11, 46, 30, 385036)),
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 8, 11, 46, 30, 385036)),
        ),
    ]
