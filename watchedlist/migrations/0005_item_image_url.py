# Generated by Django 5.1 on 2025-01-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchedlist', '0004_alter_item_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
