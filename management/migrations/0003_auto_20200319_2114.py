# Generated by Django 3.0.4 on 2020-03-19 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_garbagecategory_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='garbagecategory',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='Garbage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('price', models.FloatField(default=0.0)),
                ('weight', models.PositiveIntegerField(blank=True)),
                ('image', models.ImageField(upload_to='garbage_product')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('uploaded_by', models.IntegerField(default=0)),
                ('categoy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.GarbageCategory')),
            ],
        ),
    ]
