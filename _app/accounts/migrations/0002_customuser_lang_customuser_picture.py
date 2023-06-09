# Generated by Django 4.2.1 on 2023-06-08 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='lang',
            field=models.CharField(choices=[('ru', 'Russian'), ('en', 'English')], default='ru', max_length=3),
        ),
        migrations.AddField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
