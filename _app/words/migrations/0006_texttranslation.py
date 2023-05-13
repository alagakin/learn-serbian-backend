# Generated by Django 4.2.1 on 2023-05-11 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0005_text_word_texts'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('lang', models.CharField(choices=[('ru', 'Russian'), ('eng', 'English')], max_length=3)),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='words.text')),
            ],
        ),
    ]