# Generated by Django 2.1.2 on 2018-12-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0015_auto_20181230_0629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageupload',
            name='title',
        ),
        migrations.AddField(
            model_name='imageuploadfile',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
