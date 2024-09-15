import boto3
import uuid
import random
import json
import datetime
import time
from botocore.exceptions import ClientError
from decimal import Decimal

# Configuración de productos y repartidores (con precios como Decimal)
productos = [
    {"IdProducto": "pk0001", "producto": "Moneda", "precio": Decimal('1.00')},
    {"IdProducto": "pk0002", "producto": "Estuche para gafas", "precio": Decimal('8.00')},
    {"IdProducto": "pk0003", "producto": "Pequeño espejo de bolsillo", "precio": Decimal('5.00')},
    {"IdProducto": "pk0004", "producto": "Pendrive", "precio": Decimal('12.00')},
    {"IdProducto": "pk0005", "producto": "Tarjeta SIM", "precio": Decimal('3.00')},
    {"IdProducto": "pk0006", "producto": "Adaptador de corriente", "precio": Decimal('10.00')},
    {"IdProducto": "pk0007", "producto": "Tijeras pequeñas", "precio": Decimal('4.00')},
    {"IdProducto": "pk0008", "producto": "Pila de botón", "precio": Decimal('2.50')},
    {"IdProducto": "pk0009", "producto": "Goma de borrar", "precio": Decimal('0.50')},
    {"IdProducto": "pk0010", "producto": "Clip sujetapapeles", "precio": Decimal('0.20')}
]

repartidores = [
    {"IdRepartidor": 101, "Nombre": "María López"},
    {"IdRepartidor": 102, "Nombre": "Carlos García"},
    {"IdRepartidor": 103, "Nombre": "Ana Fernández"},
    {"IdRepartidor": 104, "Nombre": "Juan Martínez"},
    {"IdRepartidor": 105, "Nombre": "Laura Sánchez"},
    {"IdRepartidor": 106, "Nombre": "Pedro Gómez"},
    {"IdRepartidor": 107, "Nombre": "Elena Rodríguez"},
    {"IdRepartidor": 108, "Nombre": "Jorge Pérez"},
    {"IdRepartidor": 109, "Nombre": "Sofía Morales"},
    {"IdRepartidor": 110, "Nombre": "Daniel Castillo"}
]

# Configuración de DynamoDB para LocalStack
dynamodb = boto3.resource('dynamodb',
                          endpoint_url='http://localhost:4566',
                          region_name='us-east-1',
                          aws_access_key_id='test',
                          aws_secret_access_key='test')
table = dynamodb.Table('Entregas')

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def registrar_pedido_entregado(pedido_id, repartidor, productos_entrega):
    try:
        item = {
            'pedido_id': pedido_id,
            'repartidor': {
                'id_repartidor': repartidor['IdRepartidor'],
                'nombre': repartidor['Nombre']
            },
            'productos': [
                {
                    'id_producto': p['IdProducto'],
                    'nombre': p['producto'],
                    'precio': p['precio']
                } for p in productos_entrega
            ],
            'cantidad_productos': len(productos_entrega),
            'direccion_entrega': f"Calle {random.randint(1, 100)}, Ciudad",
            'fecha_entrega': datetime.datetime.now().isoformat()
        }
        
        table.put_item(Item=item)
        print(json.dumps(item, indent=2, ensure_ascii=False, default=decimal_default))
        print("### Pedido entregado, registrado exitosamente en DynamoDB")
    except ClientError as e:
        print(f"Error al guardar la entrega en DynamoDB: {e.response['Error']['Message']}")

while True:
    try:
        pedido_id = f"ENT-{str(uuid.uuid4())[:8]}"
        repartidor = random.choice(repartidores)
        productos_entrega = random.choices(productos, k=random.randint(1, 5))

        registrar_pedido_entregado(pedido_id, repartidor, productos_entrega)
        time.sleep(5)
    except KeyboardInterrupt:
        print("Script interrumpido por el usuario.")
        break
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        time.sleep(5)