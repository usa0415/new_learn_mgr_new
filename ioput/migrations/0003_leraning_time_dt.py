# Generated by Django 3.1.6 on 2021-03-13 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ioput', '0002_leraning_time_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='leraning_time',
            name='dt',
            field=models.DateTimeField(null=True),
        ),
    ]
