import boto3
from botocore.exceptions import ClientError
from ..domain.models import Metricas, PedidoEntregado
from ..domain.repositories import MonitoreoRepository
import os
from collections import Counter

class DynamoDBMonitoreoRepository(MonitoreoRepository):
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566')
        self.table = self.dynamodb.Table(os.environ['MONITOREO_TABLE_NAME'])

    def obtener_metricas(self) -> Metricas:
        try:
            response = self.table.scan()
            pedidos = [PedidoEntregado(**item) for item in response.get('Items', [])]
            
            entregas_por_repartidor = Counter(pedido.repartidor for pedido in pedidos)
            
            productos = [producto for pedido in pedidos for producto in pedido.productos]
            productos_mas_vendidos = Counter(producto['id'] for producto in productos)
            
            return Metricas(
                entregas_por_repartidor=dict(entregas_por_repartidor),
                productos_mas_vendidos=dict(productos_mas_vendidos)
            )
        except ClientError as e:
            print(f"Error al obtener las métricas: {e.response['Error']['Message']}")
            raise