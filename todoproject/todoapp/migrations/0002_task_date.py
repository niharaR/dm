# Generated by Django 4.1.5 on 2023-02-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-08-29'),
            preserve_default=False,
        ),
    ]