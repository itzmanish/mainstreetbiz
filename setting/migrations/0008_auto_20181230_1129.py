# Generated by Django 2.1.2 on 2018-12-30 11:29

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0007_auto_20181229_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyingprocess',
            name='buying',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
