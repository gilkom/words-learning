# Generated by Django 5.0.2 on 2024-02-18 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nauka', '0003_learn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='repetiion_types',
            new_name='repetition_types',
        ),
    ]
