# Generated by Django 2.1.2 on 2019-01-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0016_auto_20190127_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metatags',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metatags',
            name='meta_keywords',
            field=models.TextField(blank=True, null=True),
        ),
    ]
