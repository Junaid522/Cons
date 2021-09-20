# Generated by Django 3.1.2 on 2021-07-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0033_auto_20210617_0557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scholarship',
            options={'ordering': ('scholarship_name',)},
        ),
        migrations.AddField(
            model_name='currency',
            name='value_to_pkr',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]