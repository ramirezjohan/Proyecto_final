
from .base_generator import BaseGenerator

class CGenerator(BaseGenerator):
    def generate(self, mcu, peripherals):
        code = f"// Código generado para {mcu.modelo}\n"
        for p in peripherals:
            code += f"// Inicializar {p.name} ({p.peripheral_type})\n"
        return code
