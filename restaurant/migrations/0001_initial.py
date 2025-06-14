# Generated by Django 5.2.1 on 2025-05-27 11:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(11)])),
                ('name', models.CharField(max_length=255)),
                ('no_of_guests', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(6)])),
                ('booking_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(5)])),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('inventory', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
            ],
        ),
    ]
