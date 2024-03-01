from django.urls import path

from catalog.views import index, contact, product_info
from catalog import apps

app_name = apps.CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contact),
    path('<int:pk>/', product_info, name='product_info')
]