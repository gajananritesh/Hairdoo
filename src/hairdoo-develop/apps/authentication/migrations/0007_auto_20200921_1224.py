# Generated by Django 3.1 on 2020-09-21 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20200921_1223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='Social_id',
            new_name='social_id',
        ),
    ]
