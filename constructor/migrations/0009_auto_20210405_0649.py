# Generated by Django 3.1.2 on 2021-04-05 06:49

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0008_auto_20210309_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='institute_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]