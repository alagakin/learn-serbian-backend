# Generated by Django 4.2.1 on 2023-05-26 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0015_word_s3_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SavedWord',
        ),
    ]