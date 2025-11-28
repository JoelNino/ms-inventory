from django.http import JsonResponse
from inventario.models import InventoryStock, Product


def stock_por_producto(request, sku):
    """
    Query → Retorna el stock por ciudad de un producto.
    GET /inventory/stock/P01/
    """
    try:
        product = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Producto no encontrado"}, status=404)

    registros = InventoryStock.objects.filter(product=product)

    resultado = [
        {"city": r.city.name, "stock": r.quantity}
        for r in registros
    ]

    return JsonResponse({
        "sku": sku,
        "stock_por_ciudad": resultado
    })
