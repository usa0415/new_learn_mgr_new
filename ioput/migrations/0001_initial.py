# Generated by Django 3.1.6 on 2021-02-21 02:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='leraning_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdt', models.DateTimeField(default=django.utils.timezone.now)),
                ('enddt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
