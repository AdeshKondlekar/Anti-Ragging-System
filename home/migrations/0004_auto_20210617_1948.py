# Generated by Django 3.2.3 on 2021-06-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='signup',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
