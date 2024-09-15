from dataclasses import dataclass
from typing import List
import datetime

@dataclass
class Producto:
    id_producto: str
    nombre: str
    precio: float

@dataclass
class Repartidor:
    id_repartidor: int
    nombre: str

@dataclass
class Entrega:
    pedido_id: str
    repartidor: Repartidor
    productos: List[Producto]
    timestamp: datetime.datetime