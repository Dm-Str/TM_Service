# Generated by Django 5.1.2 on 2024-10-19 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='сurrency',
            new_name='currency',
        ),
    ]
