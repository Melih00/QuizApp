# Generated by Django 3.2.9 on 2021-12-04 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_alter_answer_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.CharField(choices=[('Math', 'Math'), ('General Culture', 'General Culture'), ('Music', 'Music'), ('Movies & Series', 'Movies & Series'), ('Other', 'Other')], max_length=50),
        ),
    ]
