from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    seller_email = models.EmailField()
    description = models.TextField()
    price = models.IntegerField()
    expire_at = models.DateField()
    discount_precent = models.FloatField()

    def __str__(self):
        return self.name