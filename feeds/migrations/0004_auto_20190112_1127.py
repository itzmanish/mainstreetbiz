# Generated by Django 2.1.2 on 2019-01-12 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_auto_20190112_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedpost',
            name='published',
        ),
        migrations.AddField(
            model_name='feedpost',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
