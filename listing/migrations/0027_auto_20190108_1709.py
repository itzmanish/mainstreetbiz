# Generated by Django 2.1.2 on 2019-01-08 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0026_businesslisting_testimagefield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='area_slug',
        ),
        migrations.RemoveField(
            model_name='business_type',
            name='business_type_slug',
        ),
    ]
