# Generated by Django 3.1 on 2020-11-09 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='orderdetail',
            name='earliest',
            field=models.DateTimeField(blank=True, default='', null=True),
        ),
    ]