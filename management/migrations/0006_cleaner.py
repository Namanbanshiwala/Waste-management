# Generated by Django 3.0.4 on 2020-03-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_delete_cleaner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('cleaning_task', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('price', models.FloatField(default=0.0)),
                ('address', models.TextField()),
                ('image', models.ImageField(upload_to='cleaner/')),
            ],
            options={
                'verbose_name_plural': 'Cleaners',
            },
        ),
    ]
