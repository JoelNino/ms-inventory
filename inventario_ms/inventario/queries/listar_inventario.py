from django.http import JsonResponse
from inventario.models import InventoryStock

def listar_inventario(request):
    registros = InventoryStock.objects.all().values(
        "product_id",
        "city",
        "quantity",
        "last_updated"
    )

    return JsonResponse(list(registros), safe=False)
