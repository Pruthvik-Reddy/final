# Generated by Django 2.1.3 on 2018-12-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slots',
            name='number',
            field=models.IntegerField(),
        ),
    ]
