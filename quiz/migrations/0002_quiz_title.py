# Generated by Django 3.2.9 on 2021-12-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='title',
            field=models.CharField(default=1, max_length=70),
            preserve_default=False,
        ),
    ]