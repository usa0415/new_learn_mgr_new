# Generated by Django 3.1.7 on 2021-03-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ioput', '0005_remove_leraning_time_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leraning_time',
            name='details',
            field=models.CharField(default='', max_length=200),
        ),
    ]
