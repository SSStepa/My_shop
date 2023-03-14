from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:page>/', views.IndexView.as_view(), name='index_previous'),
    path('<int:page>/', views.IndexView.as_view(), name='index_next'),
]