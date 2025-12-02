from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from inventario.models import InventoryStock

@csrf_exempt
def reset_inventory(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    borrados = InventoryStock.objects.all().delete()

    return JsonResponse({
        "message": "Inventario eliminado",
        "registros_borrados": borrados[0]
    })
