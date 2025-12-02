from django.http import JsonResponse
from inventario.models import InventoryStock

def stock_por_producto(request, product_id):
    registros = InventoryStock.objects.filter(product_id=product_id)

    resultado = [
        {"city": r.city, "quantity": r.quantity}
        for r in registros
    ]

    return JsonResponse({
        "product_id": product_id,
        "stock_por_ciudad": resultado
    })
