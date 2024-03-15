from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ContactView(TemplateView):
    template_name = 'catalog/contact.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_info.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    pass