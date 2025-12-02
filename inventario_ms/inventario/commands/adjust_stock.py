from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from inventario.models import InventoryStock

@csrf_exempt
def adjust_stock(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "JSON inválido"}, status=400)

    product_id = data.get("product_id")   # String tipo "P001"
    city = data.get("city")               # String tipo "Bogotá"
    quantity = data.get("quantity")       # Número

    if not product_id or not city or quantity is None:
        return JsonResponse({"error": "Faltan campos"}, status=400)

    # 🔥 Ahora sí: crea registro automático si no existe
    stock, created = InventoryStock.objects.get_or_create(
        product_id=product_id,
        city=city,
        defaults={"quantity": quantity}
    )

    # Si ya existía, suma cantidad
    if not created:
        stock.quantity += quantity
        stock.save()

    return JsonResponse({
        "message": "Stock actualizado",
        "created": created,
        "product_id": product_id,
        "city": city,
        "quantity": stock.quantity
    })
