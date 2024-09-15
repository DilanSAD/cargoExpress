from abc import ABC, abstractmethod
from .models import Entrega

class EntregaRepository(ABC):
    @abstractmethod
    def guardar_entrega(self, entrega: Entrega):
        pass