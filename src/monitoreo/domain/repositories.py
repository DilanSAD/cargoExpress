from abc import ABC, abstractmethod
from .models import Metricas

class MonitoreoRepository(ABC):
    @abstractmethod
    def obtener_metricas(self) -> Metricas:
        pass