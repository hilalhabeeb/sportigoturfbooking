# Generated by Django 4.2.7 on 2023-11-13 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurfProvider',
            fields=[
                ('venue_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('contact_number', models.CharField(max_length=15)),
                ('document', models.FileField(upload_to='documents/')),
                ('sports_type', models.CharField(choices=[('football', 'Football'), ('cricket', 'Cricket')], max_length=10)),
                ('address', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=False)),
                ('random_password', models.CharField(blank=True, max_length=20, null=True)),
                ('password_updated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TurfListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turf_name', models.CharField(max_length=255)),
                ('sports_type', models.CharField(choices=[('football', 'Football'), ('cricket', 'Cricket')], max_length=10)),
                ('description', models.TextField()),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=100)),
                ('is_available', models.BooleanField(default=True)),
                ('available_from', models.TimeField()),
                ('available_to', models.TimeField()),
                ('image', models.ImageField(upload_to='turf_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('turf_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.turfprovider')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('turf_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.turflisting')),
                ('turf_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.turfprovider')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
