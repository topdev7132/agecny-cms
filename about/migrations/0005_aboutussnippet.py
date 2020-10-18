# Generated by Django 3.0.5 on 2020-06-09 08:34

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('about', '0004_auto_20200609_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Overwrites the default title', max_length=50)),
                ('text', wagtail.core.fields.RichTextField()),
                ('content_title', wagtail.core.fields.RichTextField()),
                ('content_text', wagtail.core.fields.RichTextField()),
                ('alphabet_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
    ]