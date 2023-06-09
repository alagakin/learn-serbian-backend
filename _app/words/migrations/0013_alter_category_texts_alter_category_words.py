# Generated by Django 4.2.1 on 2023-05-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0012_savedword_deleted_alter_category_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='texts',
            field=models.ManyToManyField(blank=True, related_name='categories', to='words.text'),
        ),
        migrations.AlterField(
            model_name='category',
            name='words',
            field=models.ManyToManyField(blank=True, related_name='categories', to='words.word'),
        ),
    ]
