from ..domain.models import Metricas
from ..domain.repositories import MonitoreoRepository

class MonitoreoService:
    def __init__(self, repository: MonitoreoRepository):
        self.repository = repository

    def obtener_metricas(self) -> Metricas:
        return self.repository.obtener_metricas()