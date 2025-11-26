from django.urls import path
from .views import stock_por_producto

urlpatterns = [
    path('productos/<int:product_id>/stock/', stock_por_producto),
]
