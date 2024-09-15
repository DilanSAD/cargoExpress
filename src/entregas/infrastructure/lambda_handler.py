import os
import json
import boto3
from datetime import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:4566')
table = dynamodb.Table(os.environ['ENTREGAS_TABLE_NAME'])

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    try:
        body = json.loads(event['body'])
        logger.info(f"Parsed body: {json.dumps(body)}")
        
        pedido = {
            'pedido_id': body['id'],
            'repartidor': {
                'id_repartidor': int(body['repartidor_id']),
                'nombre': body['repartidor_nombre']
            },
            'productos': body['productos'],
            'timestamp': body['fecha_entrega']
        }
        logger.info(f"Attempting to put item: {json.dumps(pedido)}")
        
        response = table.put_item(Item=pedido)
        logger.info(f"DynamoDB response: {json.dumps(response)}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Pedido registrado exitosamente'})
        }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Error al registrar el pedido', 'error': str(e)})
        }