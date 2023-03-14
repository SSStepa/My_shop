from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField(null=True)
    img = models.ImageField(upload_to='./images', null=True, blank=True)
