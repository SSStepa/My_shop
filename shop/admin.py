from django.contrib import admin

from .models import (
    CategoryModel,
    ProductModel,
)

admin.site.register(ProductModel)
admin.site.register(CategoryModel)
