# Generated by Django 3.2.3 on 2021-06-17 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_signup_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='file',
            field=models.ImageField(blank=True, upload_to='img/images'),
        ),
    ]
