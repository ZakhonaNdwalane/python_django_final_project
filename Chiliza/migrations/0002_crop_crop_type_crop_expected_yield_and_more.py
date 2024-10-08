# Generated by Django 5.1.1 on 2024-09-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chiliza', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='crop_type',
            field=models.CharField(choices=[('cash', 'Cash Crop'), ('staple', 'Staple Crop')], default='cash', max_length=100),
        ),
        migrations.AddField(
            model_name='crop',
            name='expected_yield',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='crop',
            name='harvesting_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='crop',
            name='planting_period',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='co2_emissions',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='fertilizer_used',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='labor_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='water_used',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='climate_zone',
            field=models.CharField(default='Temperate', max_length=100),
        ),
        migrations.AddField(
            model_name='farm',
            name='contact_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='soil_type',
            field=models.CharField(default='Loamy', max_length=100),
        ),
    ]
