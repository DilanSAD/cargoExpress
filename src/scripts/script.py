import requests
import uuid
import random
import json
import datetime
import time

productos = [
    {
        "IdProducto": "pk0001",
        "producto": "Moneda",
        "precio": 1.00
    },
    {
        "IdProducto": "pk0002",
        "producto": "Estuche para gafas",
        "precio": 8.00
    },
    {
        "IdProducto": "pk0003",
        "producto": "Pequeño espejo de bolsillo",
        "precio": 5.00
    },
    {
        "IdProducto": "pk0004",
        "producto": "Pendrive",
        "precio": 12.00
    },
    {
        "IdProducto": "pk0005",
        "producto": "Tarjeta SIM",
        "precio": 3.00
    },
    {
        "IdProducto": "pk0006",
        "producto": "Adaptador de corriente",
        "precio": 10.00
    },
    {
        "IdProducto": "pk0007",
        "producto": "Tijeras pequeñas",
        "precio": 4.00
    },
    {
        "IdProducto": "pk0008",
        "producto": "Pila de botón",
        "precio": 2.50
    },
    {
        "IdProducto": "pk0009",
        "producto": "Goma de borrar",
        "precio": 0.50
    },
    {
        "IdProducto": "pk0010",
        "producto": "Clip sujetapapeles",
        "precio": 0.20
    }
]

repartidores = [
    {
        "IdRepartidor": 101,
        "Nombre": "María López"
    },
    {
        "IdRepartidor": 102,
        "Nombre": "Carlos García"
    },
    {
        "IdRepartidor": 103,
        "Nombre": "Ana Fernández"
    },
    {
        "IdRepartidor": 104,
        "Nombre": "Juan Martínez"
    },
    {
        "IdRepartidor": 105,
        "Nombre": "Laura Sánchez"
    },
    {
        "IdRepartidor": 106,
        "Nombre": "Pedro Gómez"
    },
    {
        "IdRepartidor": 107,
        "Nombre": "Elena Rodríguez"
    },
    {
        "IdRepartidor": 108,
        "Nombre": "Jorge Pérez"
    },
    {
        "IdRepartidor": 109,
        "Nombre": "Sofía Morales"
    },
    {
        "IdRepartidor": 110,
        "Nombre": "Daniel Castillo"
    }
]

def registrar_pedido_entregado(pedido_id, repartidor, productos):
    url = "http://localhost:4566/restapis/[]/prod/entregas"
    payload = {
        "id": pedido_id,
        "repartidor_id": str(repartidor["IdRepartidor"]),
        "repartidor_nombre": repartidor["Nombre"],
        "productos": [{"id": p["IdProducto"], "nombre": p["producto"], "precio": p["precio"]} for p in productos],
        "cantidad_productos": len(productos),
        "direccion_entrega": f"Calle {random.randint(1, 100)}, Ciudad",
        "fecha_entrega": datetime.datetime.now().isoformat()
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        print("### Pedido entregado, registrado exitosamente")
    else:
        print(f"### Error al registrar el pedido entregado: {response.status_code} - {response.text}")

while True:
    pedido_id = f"ENT-{str(uuid.uuid4())[:8]}"
    repartidor = random.choice(repartidores)
    productos_entrega = random.choices(productos, k=random.randint(1, 5))

    registrar_pedido_entregado(pedido_id, repartidor, productos_entrega)
    time.sleep(5)
