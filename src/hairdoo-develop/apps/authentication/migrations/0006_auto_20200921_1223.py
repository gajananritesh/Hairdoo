# Generated by Django 3.1 on 2020-09-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20200918_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='Social_id',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
    ]
