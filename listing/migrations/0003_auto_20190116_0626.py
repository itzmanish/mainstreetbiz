# Generated by Django 2.1.2 on 2019-01-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_auto_20190116_0559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businesslisting',
            options={'ordering': ['my_order']},
        ),
        migrations.AddField(
            model_name='businesslisting',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
