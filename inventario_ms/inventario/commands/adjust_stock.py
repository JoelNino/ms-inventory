import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction

from inventario.models import Product, City, InventoryStock


@csrf_exempt
@transaction.atomic
def adjust_stock(request):
    """
    Command → Ajusta el stock de un producto en una ciudad.
    Espera:
    {
        "sku": "P01",
        "city": "Bogotá",
        "quantity": 50
    }
    """
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    try:
        data = json.loads(request.body)
        sku = data["sku"]
        city_name = data["city"]
        quantity = int(data["quantity"])
    except:
        return JsonResponse({"error": "JSON inválido"}, status=400)

    product = Product.objects.get(sku=sku)
    city, _ = City.objects.get_or_create(name=city_name)

    stock_obj, created = InventoryStock.objects.get_or_create(
        product=product,
        city=city,
        defaults={"quantity": quantity}
    )

    if not created:
        stock_obj.quantity = quantity
        stock_obj.save()

    return JsonResponse({
        "message": "Stock actualizado correctamente",
        "sku": sku,
        "city": city.name,
        "new_quantity": stock_obj.quantity
    })
