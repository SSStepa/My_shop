
from django.shortcuts import render
from django.views import generic
from .models import Product
from django.core.paginator import Paginator

class IndexView(generic.ListView):
    template_name = 'shop/index.html'
    context_object_name = 'page_list'
    model = Product
    paginate_by = 5
