# Generated by Django 3.0.5 on 2020-04-12 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('url', models.URLField(verbose_name='original version of the URL')),
                ('slug', models.SlugField(max_length=7, verbose_name='shortened version of the URL')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='number of visitors to this slug')),
            ],
        ),
    ]
