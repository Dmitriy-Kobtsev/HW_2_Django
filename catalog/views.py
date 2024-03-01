from django.shortcuts import render
from catalog.models import Product


def index(request):
    products = Product.objects.all()
    context = {
        'object_list': products,
    }
    return render(request, 'catalog/index.html', context)


def contact(request):
    return render(request, 'catalog/contact.html')


def product_info(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'object': product,
    }
    return render(request, 'catalog/product_info.html', context)
