from django.urls import path

from . import views

app_name = "shop"
urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("<int:category_id>/", views.IndexCategoryView.as_view(), name="index"),
    path("detail/<int:product_id>/", views.DetailProductView.as_view(), name="detail"),
    path("user/sing_up/", views.RegisterUser.as_view(), name="user_register"),
    path("user/sing_in/", views.LoginUser.as_view(), name="user_login"),
]
