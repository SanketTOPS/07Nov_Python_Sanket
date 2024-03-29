# Generated by Django 4.1.4 on 2023-02-03 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 3, 11, 23, 22, 540580))),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('username', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]
