import os
import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566')
table = dynamodb.Table(os.environ['ENTREGAS_TABLE_NAME'])

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        pedido = {
            'pedido_id': body['id'],
            'repartidor': {
                'id_repartidor': int(body['repartidor_id']),
                'nombre': body['repartidor_nombre']
            },
            'productos': body['productos'],
            'timestamp': body['fecha_entrega']
        }
        table.put_item(Item=pedido)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Pedido registrado exitosamente'})
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error al registrar el pedido', 'error': str(e)})
        }