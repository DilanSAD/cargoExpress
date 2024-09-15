import boto3
from botocore.exceptions import ClientError
from ..domain.models import Entrega
from ..domain.repositories import EntregaRepository
import os

class DynamoDBEntregaRepository(EntregaRepository):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566')
        self.table = self.dynamodb.Table(os.environ['ENTREGAS_TABLE_NAME'])

    def guardar_entrega(self, entrega: Entrega):
        try:
            item = {
                'pedido_id': entrega.pedido_id,
                'repartidor': {
                    'id_repartidor': entrega.repartidor.id_repartidor,
                    'nombre': entrega.repartidor.nombre
                },
                'productos': [
                    {
                        'id_producto': p.id_producto,
                        'nombre': p.nombre,
                        'precio': p.precio
                    } for p in entrega.productos
                ],
                'timestamp': entrega.timestamp.isoformat()
            }
            self.table.put_item(Item=item)
        except ClientError as e:
            print(f"Error al guardar la entrega: {e.response['Error']['Message']}")
            raise