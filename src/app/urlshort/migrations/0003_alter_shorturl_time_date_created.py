# Generated by Django 4.2.13 on 2024-05-23 14:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('urlshort', '0002_alter_shorturl_original_url_alter_shorturl_short_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='time_date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
