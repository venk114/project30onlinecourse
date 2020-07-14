# Generated by Django 2.2.13 on 2020-07-12 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleNewClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, unique=True)),
                ('Faculty', models.CharField(max_length=50)),
                ('Date', models.DateField(default=datetime.date(2020, 1, 1))),
                ('Time', models.TimeField(default=datetime.time(2, 30, 5))),
                ('Fee', models.FloatField()),
                ('Duration', models.IntegerField()),
            ],
        ),
    ]