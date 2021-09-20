# Generated by Django 3.1.2 on 2021-06-17 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0032_topkeywords'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='discipline',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='specialization',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='topkeywords',
            name='degree_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constructor.degreelevel'),
        ),
    ]
