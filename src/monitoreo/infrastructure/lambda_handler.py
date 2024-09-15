import os
import json
import boto3
from ..application.services import MonitoreoService
from ..infrastructure.dynamodb_repository import DynamoDBMonitoreoRepository

def lambda_handler(event, context):
    try:
        repository = DynamoDBMonitoreoRepository()
        service = MonitoreoService(repository)
        metricas = service.obtener_metricas()

        return {
            'statusCode': 200,
            'body': json.dumps({
                'entregas_por_repartidor': metricas.entregas_por_repartidor,
                'productos_mas_vendidos': metricas.productos_mas_vendidos
            })
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error al obtener las métricas', 'error': str(e)})
        }