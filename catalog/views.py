from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def contact(request):
    return render(request, 'catalog/contact.html')
