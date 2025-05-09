from django.db import models

class SalesData(models.Model):
    date = models.DateField()
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product} on {self.date}"
