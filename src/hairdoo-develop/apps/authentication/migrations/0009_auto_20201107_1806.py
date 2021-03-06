# Generated by Django 3.1 on 2020-11-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20200924_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='hair_type',
            field=models.CharField(blank=True, choices=[('straight', 'Straight'), ('curly', 'Curly'), ('long', 'Long')], max_length=10, null=True),
        ),
    ]
