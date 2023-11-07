# Generated by Django 4.2.6 on 2023-11-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_turfprovider_random_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='turfprovider',
            name='password_updated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='turfprovider',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
