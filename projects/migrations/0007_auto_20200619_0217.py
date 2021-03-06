# Generated by Django 3.0.5 on 2020-06-19 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200619_0205'),
        ('projects', '0006_projectspage_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetailpage',
            name='navigation_bar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.NavigationSnippet'),
        ),
        migrations.AddField(
            model_name='projectspage',
            name='navigation_bar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.NavigationSnippet'),
        ),
    ]
