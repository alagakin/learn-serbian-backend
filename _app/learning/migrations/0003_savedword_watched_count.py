# Generated by Django 4.2.1 on 2023-05-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_savedword_skipped'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedword',
            name='watched_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
