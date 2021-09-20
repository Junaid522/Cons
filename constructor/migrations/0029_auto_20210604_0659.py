# Generated by Django 3.1.2 on 2021-06-04 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0028_auto_20210531_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Region Name', max_length=255, verbose_name=' Region Name')),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='city',
            name='popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='country',
            name='popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='state',
            name='popular',
            field=models.BooleanField(default=False),
        ),
    ]
