
from app.models import Peripheral

class PeripheralFactory:
    @staticmethod
    def create(peripheral_type: str, name: str, config: dict) -> Peripheral:
        # Aquí podríamos tener lógica más compleja según el tipo
         return Peripheral(peripheral_type, name, config)
