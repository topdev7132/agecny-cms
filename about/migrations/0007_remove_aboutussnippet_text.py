# Generated by Django 3.0.5 on 2020-06-09 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_aboutussnippet_bg_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutussnippet',
            name='text',
        ),
    ]
