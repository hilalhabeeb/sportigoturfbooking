# Generated by Django 4.2.7 on 2024-02-12 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_clubuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubuser',
            name='club_id',
        ),
        migrations.RemoveField(
            model_name='clubuser',
            name='mobile_number',
        ),
    ]
