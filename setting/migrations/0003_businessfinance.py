# Generated by Django 2.1.2 on 2018-12-20 08:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0002_auto_20181219_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessFinance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_finance', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]