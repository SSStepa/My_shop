from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import (
    BlockedIPModel,
    CategoryModel,
    ProductModel,
    URLFromModel,
    UserModel,
)

admin.site.unregister(Group)
admin.site.register(ProductModel)
admin.site.register(CategoryModel)
admin.site.register(UserModel, UserAdmin)
admin.site.register(BlockedIPModel)
admin.site.register(URLFromModel)
