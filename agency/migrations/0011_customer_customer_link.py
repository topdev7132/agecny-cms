# Generated by Django 3.0.5 on 2020-05-01 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0010_auto_20200501_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_link',
            field=models.URLField(blank=True, max_length=254, null=True),
        ),
    ]
