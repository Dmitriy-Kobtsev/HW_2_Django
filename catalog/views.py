from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ContactView(TemplateView):
    template_name = 'catalog/contact.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_info.html'