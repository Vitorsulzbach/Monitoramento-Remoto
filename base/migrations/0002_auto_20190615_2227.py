# Generated by Django 2.1.7 on 2019-06-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graphic',
            name='date1',
        ),
        migrations.AddField(
            model_name='graphic',
            name='year',
            field=models.CharField(default=1900, max_length=4),
            preserve_default=False,
        ),
    ]