# Generated by Django 2.1.7 on 2019-06-16 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20190616_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graphic',
            name='name',
        ),
    ]
