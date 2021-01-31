# Generated by Django 3.1 on 2020-09-16 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('profile_image', models.ImageField(upload_to='artist_profile')),
                ('email', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_address', models.TextField()),
                ('apt_no', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=500)),
                ('note', models.TextField(blank=True, null=True)),
                ('earliest', models.DateTimeField(blank=True, null=True)),
                ('latest', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField()),
                ('is_complete', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('SENT', 'Sent'), ('CONFIRM', 'Confirm'), ('ON_WAY', 'On Way'), ('ARRIVING', 'Arriving'), ('PROGRESS', 'Progress'), ('COMPLETE', 'Complete')], default='SENT', max_length=15)),
                ('is_reorder', models.BooleanField(default=False)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.artist')),
                ('book_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.orderdetail')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.service')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
