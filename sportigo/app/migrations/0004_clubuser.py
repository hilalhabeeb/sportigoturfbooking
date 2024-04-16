# Generated by Django 4.2.7 on 2024-02-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_turflisting_image_turfimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubUser',
            fields=[
                ('club_id', models.CharField(max_length=50, unique=True)),
                ('club_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('contact_number', models.CharField(max_length=15)),
                ('document', models.FileField(upload_to='club_documents/')),
                ('address', models.TextField()),
                ('mobile_number', models.CharField(max_length=15)),
                ('is_active', models.BooleanField(default=False)),
                ('random_password', models.CharField(blank=True, max_length=20, null=True)),
                ('password_updated', models.BooleanField(default=False)),
            ],
        ),
    ]