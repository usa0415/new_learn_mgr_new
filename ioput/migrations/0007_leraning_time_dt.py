# Generated by Django 3.1.7 on 2021-03-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ioput', '0006_auto_20210315_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='leraning_time',
            name='dt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
