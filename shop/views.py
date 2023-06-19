from django.contrib.auth.forms import AuthenticationForm
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
from django.views import generic
from django.views.generic import CreateView

from .forms import UserForm
from .models import (
    CategoryModel,
    ProductModel,
)


class IndexView(generic.ListView):
    model = ProductModel
    template_name = "shop/index.html"
    context_object_name = "products"
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        context["categories_breadcrumbs"] = None
        return context


class IndexCategoryView(generic.ListView):
    model = ProductModel
    template_name = "shop/index.html"
    context_object_name = "products"
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        category = get_object_or_404(CategoryModel, id=self.kwargs["category_id"])
        context["categories_breadcrumb"] = find_category(category, [])
        return context

    def get_queryset(self):
        return ProductModel.objects.filter(category__id=self.kwargs["category_id"])


class DetailProductView(generic.DetailView):
    model = ProductModel
    template_name = "shop/detail.html"
    pk_url_kwarg = "product_id"
    context_object_name = "product"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryModel.objects.all()
        product = get_object_or_404(ProductModel, id=self.kwargs["product_id"])
        context["categories_breadcrumb"] = find_category(product.category, [])
        return context


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
