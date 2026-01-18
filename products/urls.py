from django.urls import path
from . views import create_product, list_products, update_product, delete_product

urlpatterns = [
    path('', list_products),
    path('create/', create_product),
    path('<int:pk>/', update_product),
    path('<int:pk>/delete/', delete_product),
]