# Generated by Django 4.0.5 on 2022-06-24 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillin',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
