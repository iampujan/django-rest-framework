from django.urls import path
from .views import my_product

urlpatterns = [
    path('product',my_product, name='product-api-list-create'),
]