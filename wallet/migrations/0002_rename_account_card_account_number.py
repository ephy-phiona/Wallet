# Generated by Django 4.1 on 2022-08-25 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='account',
            new_name='account_number',
        ),
    ]
