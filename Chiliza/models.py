from django.db import models
from django.core.validators import MinValueValidator

# Model for different Farms
class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    soil_type = models.CharField(max_length=100, default='Loamy')
    climate_zone = models.CharField(max_length=100, default='Temperate')
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Model for different Crops grown on Farms
class Crop(models.Model):
    class CropType(models.TextChoices):
        CASH = 'cash', 'Cash Crop'
        STAPLE = 'staple', 'Staple Crop'

    name = models.CharField(max_length=100)
    crop_type = models.CharField(
        max_length=100,
        choices=CropType.choices,
        default=CropType.CASH  # Provide a default value here
    )
    season = models.CharField(max_length=100)  # Example: 'Summer', 'Winter'
    expected_yield = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    planting_period = models.DateField(null=True, blank=True)
    harvesting_period = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

# Model for farm data entries (e.g., crop yield, costs, etc.)
class DataEntry(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='data_entries')
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, related_name='data_entries')
    date = models.DateField()  # Date of the data entry
    yield_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]  # Ensure yield is non-negative
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]  # Ensure cost is non-negative
    )
    profit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)]  # Ensure profit is non-negative if provided
    )
    
    # Additional fields
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])  # Labor costs
    fertilizer_used = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])  # Fertilizer in kg
    water_used = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])  # Water in liters
    co2_emissions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])  # CO2 emissions in tons
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.farm.name} - {self.crop.name} - {self.date}"
