# Generated by Django 2.1.2 on 2019-01-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0006_auto_20190118_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesslisting',
            name='listing_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='commerciallisting',
            name='listing_id',
            field=models.IntegerField(unique=True),
        ),
    ]
