# Generated by Django 5.0.3 on 2024-04-03 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_location_address_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.location'),
        ),
    ]
