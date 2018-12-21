# Generated by Django 2.1.2 on 2018-12-20 09:16

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0003_businessfinance'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellingProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selling', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='businessfinance',
            name='business_finance',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]