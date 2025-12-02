from django.urls import path
from inventario.commands.adjust_stock import adjust_stock
from inventario.queries.stock_por_producto import stock_por_producto
from inventario.queries.listar_inventario import listar_inventario
from inventario.commands.reset_inventory import reset_inventory   # 👈 IMPORT QUE FALTABA

urlpatterns = [
    path("inventario/adjust-stock/", adjust_stock),
    path("inventario/stock/<str:product_id>/", stock_por_producto),
    path("inventario/todos/", listar_inventario),
    path("inventario/remove-all/", reset_inventory),  # 👈 YA FUNCIONA
]
