# Generated by Django 2.2.3 on 2020-03-17 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='viewcount',
            field=models.IntegerField(default=0),
        ),
    ]
