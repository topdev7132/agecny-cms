# Generated by Django 3.0.5 on 2020-05-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0004_auto_20200427_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('psition', models.CharField(max_length=30)),
                ('profile_link', models.URLField()),
                ('photo', models.ImageField(default='../static/img/customer/customer-1.png', upload_to='customer/')),
            ],
        ),
    ]
