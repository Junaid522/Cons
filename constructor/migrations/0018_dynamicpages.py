# Generated by Django 3.1.2 on 2021-04-26 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0017_auto_20210421_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='DynamicPages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Page Name', max_length=255, verbose_name='Name')),
                ('type', models.CharField(choices=[('privacy', 'Privacy'), ('terms', 'Terms')], max_length=50, unique=True)),
                ('heading', models.CharField(help_text='Page heading', max_length=255, verbose_name='heading')),
                ('content', models.TextField(help_text='content', verbose_name='content')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-updated_at', '-created_at'),
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
    ]
