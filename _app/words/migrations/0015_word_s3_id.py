# Generated by Django 4.2.1 on 2023-05-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0014_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='s3_id',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
