from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    CategoryModel,
    ProductModel,
    UserModel,
)

admin.site.register(ProductModel)
admin.site.register(CategoryModel)
admin.site.register(UserModel, UserAdmin)
