# Generated by Django 4.0.5 on 2022-06-25 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_fillin_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(blank=True, max_length=200, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
