from django.db import models

class Location(models.Model):
    location_form = models.CharField(max_length=100)

    def __str__(self):
        return self.location_form

class Material(models.Model):
    material_form = models.CharField(max_length=100)

    def __str__(self):
        return self.material_form

class Inventory(models.Model):
    material_code = models.CharField(max_length=10)
    material_description = models.CharField(max_length=300)
    order_quantity = models.IntegerField(default=0)
    material_type = models.ForeignKey(Material, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    quantity_issued = models.IntegerField(default=0)

    
