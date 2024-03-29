# Generated by Django 2.1.2 on 2018-12-20 13:02

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('business_involved_in', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=50)),
                ('comment', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
