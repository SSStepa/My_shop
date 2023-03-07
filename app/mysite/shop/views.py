
from django.shortcuts import render
from django.views import generic
from .models import Product
from django.core.paginator import Paginator

class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'page_list'


    def get_queryset(self, number=1):
        products =Product.objects.all()
        products_pagination = Paginator(products, 10)
        page = products_pagination.get_page(number)
        return page