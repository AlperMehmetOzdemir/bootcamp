# Generated by Django 3.2.9 on 2021-12-01 05:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('line_one', models.CharField(max_length=511, verbose_name='Line One')),
                ('line_two', models.CharField(max_length=511, verbose_name='Line Two')),
                ('phone', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message="Enter phone number in the following format: '+xxxxxxxxxxxx'. Up to 15 digits including country code.", regex='^\\+?\\d{9,15}$')], verbose_name='Phone Number')),
                ('district', models.CharField(max_length=255, verbose_name='District')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.city')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]