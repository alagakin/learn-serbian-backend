# Generated by Django 4.2.1 on 2023-05-16 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0011_tag_word_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedword',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
