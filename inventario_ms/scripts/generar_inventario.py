import requests
import random
import time

# Endpoint del microservicio de inventario
INVENTORY_URL = "http://127.0.0.1:8001/api/inventario/adjust-stock/"

# 500 productos: P001 - P500
PRODUCT_IDS = [f"P{str(i).zfill(3)}" for i in range(1, 501)]

# Lista de ciudades posibles
CIUDADES = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Bucaramanga"]

def generar_inventario():
    total_registros = 0

    for product_id in PRODUCT_IDS:
        # Para cada producto, escoger entre 2 y 5 ciudades distintas
        num_ciudades = random.randint(2, len(CIUDADES))
        ciudades_producto = random.sample(CIUDADES, num_ciudades)

        for city in ciudades_producto:
            quantity = random.randint(5, 100)

            data = {
                "product_id": product_id,
                "city": city,
                "quantity": quantity
            }

            r = requests.post(INVENTORY_URL, json=data)

            if r.status_code == 200:
                total_registros += 1
            else:
                print(f"❌ Error para {product_id} - {city}: {r.status_code} -> {r.text}")

            # pequeñísima pausa para no saturar el server
            time.sleep(0.01)

    print(f"✔ Inventario generado correctamente: {total_registros} registros")

if __name__ == "__main__":
    generar_inventario()
