# Generated by Django 5.0.2 on 2024-02-12 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nauka', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='repetiion_types',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='words_to_learn',
            field=models.IntegerField(default=0, null=True),
        ),
    ]