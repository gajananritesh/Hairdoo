# Generated by Django 3.1 on 2020-11-09 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20201109_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
