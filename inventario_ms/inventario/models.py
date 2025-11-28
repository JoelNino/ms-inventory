from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.sku} - {self.name}"


class InventoryStock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('product', 'city')

    def __str__(self):
        return f"{self.product.sku} - {self.city.name}: {self.quantity}"
