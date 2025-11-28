from django.urls import path

# Commands
from inventory.commands.adjust_stock import adjust_stock

# Queries
from inventory.queries.stock_por_producto import stock_por_producto

urlpatterns = [
    # COMMANDS
    path('inventory/adjust-stock/', adjust_stock),           # POST

    # QUERIES
    path('inventory/stock/<str:sku>/', stock_por_producto),  # GET
]
