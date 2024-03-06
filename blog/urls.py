from django.urls import path

from blog import apps

app_name = apps.BlogConfig.name

urlpatterns = [
    path('create/', ..., name='create'),
    path('contacts/', ContactView.as_view(), name='contact'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_info')
]