from django.db import models
from mptt.models import (
    MPTTModel,
    TreeForeignKey,
)


class CategoryModel(MPTTModel, models.Model):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    type = models.CharField(max_length=50, null=True)

    class MPTTMeta:
        order_insertion_by = ["type", "name"]


class ProductModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    cast = models.CharField(max_length=50, null=True, blank=True)
    time = models.FloatField(null=True, blank=True)
    img = models.ImageField(upload_to="./images", null=True, blank=True)
