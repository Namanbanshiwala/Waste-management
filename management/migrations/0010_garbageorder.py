# Generated by Django 3.0.4 on 2020-03-23 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_auto_20200322_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='GarbageOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_by', models.IntegerField()),
                ('ordered_garbage', models.IntegerField()),
            ],
        ),
    ]
