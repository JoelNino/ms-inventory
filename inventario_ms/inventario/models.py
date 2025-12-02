from django.db import models

class InventoryStock(models.Model):
    product_id = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('product_id', 'city')

    def __str__(self):
        return f"{self.product_id} - {self.city}: {self.quantity}"
