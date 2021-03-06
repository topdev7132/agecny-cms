# Generated by Django 3.0.5 on 2020-06-18 12:26

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_servicespage_quotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicespage',
            name='image_slider',
            field=wagtail.core.fields.StreamField([('img', wagtail.core.blocks.StructBlock([('img', wagtail.images.blocks.ImageChooserBlock(help_text='Upload images', required=True))]))], blank=True, null=True),
        ),
    ]
