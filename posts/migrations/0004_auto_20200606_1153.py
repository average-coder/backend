# Generated by Django 3.0.6 on 2020-06-06 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200601_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]
