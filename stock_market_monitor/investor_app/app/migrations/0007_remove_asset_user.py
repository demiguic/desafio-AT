# Generated by Django 4.2.3 on 2023-07-16 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_asset_date_asset_created_at_asset_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='user',
        ),
    ]
