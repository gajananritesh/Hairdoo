# Generated by Django 3.1 on 2020-09-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20200921_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='social_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]