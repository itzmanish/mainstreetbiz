# Generated by Django 2.1.2 on 2018-12-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0005_auto_20181227_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='featured_image/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
