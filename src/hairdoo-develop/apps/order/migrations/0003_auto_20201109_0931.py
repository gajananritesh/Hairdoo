# Generated by Django 3.1 on 2020-11-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20201109_0916'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='orderdetail',
            name='earliest',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
