from dataclasses import dataclass
from typing import List
import datetime

@dataclass
class PedidoEntregado:
    pedido_id: str
    repartidor: str
    productos: List[dict]
    timestamp: datetime.datetime

@dataclass
class Metricas:
    entregas_por_repartidor: dict
    productos_mas_vendidos: dict