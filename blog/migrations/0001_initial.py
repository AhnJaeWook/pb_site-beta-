# Generated by Django 2.2.3 on 2020-03-17 08:40

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=28)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('author', models.ForeignKey(default=1, null=True, on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]