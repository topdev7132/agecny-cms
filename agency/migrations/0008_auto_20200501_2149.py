# Generated by Django 3.0.5 on 2020-05-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0007_auto_20200501_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mark',
            field=models.IntegerField(choices=[(5, 'Perfect'), (4, 'Very good'), (3, 'Good'), (2, 'Bad'), (1, 'Very Bad')], default=0),
        ),
    ]
