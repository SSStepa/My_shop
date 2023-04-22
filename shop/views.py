from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views import generic

from .models import Category, Product

# class IndexView(generic.ListView):
#    template_name = 'shop/index.html'
#    context_object_name = 'page_list'
#    model = Product
#    paginate_by = 5


def index(request, cotegory_id=None):
    if cotegory_id == None:
        product = Product.objects.all()
        cotegories = None
    else:
        cotegory = get_object_or_404(Category, id=cotegory_id)
        cotegories = find_cotegory(cotegory, [])
        product = get_list_or_404(Product, cotegory=cotegory)
    products = findeing_sons(cotegory_id)
    for i in product:
        products.append(i)
    product_paginator = Paginator(product, 1)
    page_number = request.GET.get("page")
    page = product_paginator.get_page(page_number)
    return render(
        request,
        "shop/index.html",
        {
            "page": page,
            "cotegories": Category.objects.all(),
            "cotegories_breadcrumb": cotegories,
        },
    )


def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cotegories = find_cotegory(product.cotegory, [])
    return render(
        request,
        "shop/detail.html",
        {
            "product": product,
            "cotegories": Category.objects.all(),
            "cotegories_breadcrumb": cotegories,
        },
    )


def findeing_sons(cotegory_id, products=None):
    if products == None:
        products = []
    cotegory = Category.objects._mptt_filter(parent_id=cotegory_id)
    if cotegory:
        for i in cotegory:
            product = Product.objects.filter(cotegory=i)
            for i in product:
                products.append(i)
            findeing_sons(i.id, products)
    return products


def find_cotegory(cotegory, cotegories):
    if cotegory.parent:
        cotegories = find_cotegory(cotegory.parent, cotegories)
    cotegories.append(cotegory)
    return cotegories
