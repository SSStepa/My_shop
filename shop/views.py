from django.contrib.auth.forms import (
    AuthenticationForm,
)
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
    redirect,
    render,
)
from django.urls import reverse_lazy
# from django.views import generic
from django.views.generic import CreateView
from .forms import UserForm
from .models import (
    CategoryModel,
    ProductModel,
)

# class IndexView(generic.ListView):
#     template_name = 'shop/index.html'
#     context_object_name = 'page_list'
#     model = ProductModel, CategoryModel
#     paginate_by = 5


def index(request, category_id=None):
    if category_id is None:
        product = ProductModel.objects.all()
        categories = None
        products_find = True
    else:
        category = get_object_or_404(CategoryModel, id=category_id)
        categories = find_category(category, [])
        try:
            product = get_list_or_404(ProductModel, category=category)
            products_find = True
        except Http404:
            page = None
            products_find = False
    if products_find:
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
    categories = find_category(product.category, [])
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


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "shop/user_login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy("shop:home")


class RegisterUser(CreateView):
    form_class = UserForm
    template_name = "shop/user_register.html"
    success_url = reverse_lazy("shop:user_login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))
