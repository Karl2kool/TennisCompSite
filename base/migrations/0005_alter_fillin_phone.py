# Generated by Django 4.0.5 on 2022-07-02 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fillin',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]