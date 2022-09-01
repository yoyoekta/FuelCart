from django.db import models

class FuelProduct(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    base_charge = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_charge = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    instock = models.BooleanField()
    image = models.ImageField()
    publish_date = models.DateField()
    
    def __str__(self):
        return self.title
