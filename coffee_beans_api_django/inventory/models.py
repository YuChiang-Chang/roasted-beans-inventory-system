from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class CoffeeBean(models.Model):
    name = models.CharField(max_length=100)
    roast_date = models.DateField()
    roast_level = models.CharField(max_length=50)
    weight = models.IntegerField(validators=[MinValueValidator(0)])
    origin = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.name