# Generated by Django 2.1.3 on 2018-12-08 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20181202_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 12, 8, 18, 57, 26, 771493)),
        ),
    ]
