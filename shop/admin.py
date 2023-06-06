from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import (
    CategoryModel,
    ProductModel,
    UserModel,
)

admin.site.unregister(Group)
admin.site.register(ProductModel)
admin.site.register(CategoryModel)
admin.site.register(UserModel, UserAdmin)
