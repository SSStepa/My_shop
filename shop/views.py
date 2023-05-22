from django.core.paginator import Paginator
from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
    render,
)

from .models import (
    CategoryModel,
    ProductModel,
)

# from django.views import generic


# class IndexView(generic.ListView):
#    template_name = 'shop/index.html'
#    context_object_name = 'page_list'
#    model = Product
#    paginate_by = 5


def index(request, category_id=None):
    if category_id is None:
        product = ProductModel.objects.all()
        categories = None
    else:
        category = get_object_or_404(CategoryModel, id=category_id)
        categories = find_category(category, [])
        product = get_list_or_404(ProductModel, category=category)
    products = finding_sons(category_id)
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
            "categories": CategoryModel.objects.all(),
            "categories_breadcrumb": categories,
        },
    )


def detail(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)
    categories = find_category(product.cotegory, [])
    return render(
        request,
        "shop/detail.html",
        {
            "product": product,
            "categories": CategoryModel.objects.all(),
            "categories_breadcrumb": categories,
        },
    )


def finding_sons(category_id, products=None):
    if products is None:
        products = []
    category = CategoryModel.objects._mptt_filter(parent_id=category_id)
    if category:
        for i in category:
            product = ProductModel.objects.filter(category=i)
            for x in product:
                products.append(x)
            finding_sons(i.id, products)
    return products


def find_category(category, categories):
    if category.parent:
        categories = find_category(category.parent, categories)
    categories.append(category)
    return categories
