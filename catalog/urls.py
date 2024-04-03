from django.urls import path

from catalog.views import ProductListView, ProductDetailView, ContactView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductDescriptionUpdateView
from catalog import apps

app_name = apps.CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('update/description/<int:pk>/', ProductDescriptionUpdateView.as_view(), name='product_update_description'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]