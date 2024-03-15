from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ContactView, ProductCreateView, ProductUpdateView
from catalog import apps

app_name = apps.CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update')
]