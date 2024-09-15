from ..domain.models import Entrega
from ..domain.repositories import EntregaRepository

class EntregaService:
    def __init__(self, repository: EntregaRepository):
        self.repository = repository

    def registrar_entrega(self, entrega: Entrega):
        self.repository.guardar_entrega(entrega)