# Generated by Django 3.1.1 on 2021-02-24 06:35

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParcelOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=64)),
                ('last_name', models.CharField(blank=True, max_length=64)),
                ('organization', models.CharField(blank=True, max_length=64)),
                ('address_1', models.CharField(blank=True, max_length=64)),
                ('address_2', models.CharField(blank=True, max_length=64)),
                ('email', models.EmailField(blank=True, max_length=64)),
                ('phone', models.CharField(blank=True, max_length=16)),
                ('website', models.CharField(blank=True, max_length=64)),
            ],
            options={
                'verbose_name': 'Parcel Owner',
                'verbose_name_plural': 'Parcel owners',
            },
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, null=True)),
                ('name', models.CharField(blank=True, max_length=128)),
                ('extension', models.DecimalField(blank=True, decimal_places=2, help_text='In hectares', max_digits=4, null=True)),
                ('location', django.contrib.gis.db.models.fields.PolygonField(blank=True, help_text='Select at least 3 points to delimit a region. When you have finished, press click twice.', null=True, srid=4326)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sources.parcelowner')),
            ],
            options={
                'verbose_name': 'Parcel',
                'verbose_name_plural': 'Parcels',
            },
        ),
    ]
