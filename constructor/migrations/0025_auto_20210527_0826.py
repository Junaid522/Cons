# Generated by Django 3.1.2 on 2021-05-27 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0024_faqa'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FAQA',
            new_name='CountryFAQA',
        ),
        migrations.RenameField(
            model_name='countryfaqa',
            old_name='content',
            new_name='answer',
        ),
    ]