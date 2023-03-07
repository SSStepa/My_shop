from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:number>/', views.IndexView.as_view(), name='index_previous'),
    path('<int:number>/', views.IndexView.as_view(), name='index_next'),
]