# Generated by Django 3.0.5 on 2020-06-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_navigationsnippet_facebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationsnippet',
            name='google',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='navigationsnippet',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='navigationsnippet',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='navigationsnippet',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
    ]
