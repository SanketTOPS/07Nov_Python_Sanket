# Generated by Django 4.1.4 on 2023-02-06 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mynotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 6, 11, 26, 27, 528358))),
                ('title', models.CharField(max_length=100)),
                ('cate', models.CharField(max_length=100)),
                ('myfiles', models.FileField(upload_to='Notes')),
                ('comments', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 6, 11, 26, 27, 527358)),
        ),
    ]