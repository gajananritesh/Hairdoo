# Generated by Django 3.1 on 2020-09-17 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_active',
            new_name='active',
        ),
    ]