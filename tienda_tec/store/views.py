from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from .models import Product


class ProductListView(ListView):
    template_name = 'store/product_list.html'
    model = Product
