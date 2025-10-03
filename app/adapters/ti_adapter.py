
from .base_adapter import BaseAdapter

class TIAdapter(BaseAdapter):
    def generate_code(self, peripheral):
        name = peripheral.name.upper()       # Ej: P1
        pin = peripheral.config.get("pin")   # Ej: 0
        mode = peripheral.config.get("mode").upper()

        # Validacion de puerto (P1, P2, etc.) y BITx
        if not name.startswith("P"):
            raise ValueError(f"Nombre de puerto '{name}' inválido para TI (debe comenzar con 'P').")
        
        if pin < 0 or pin > 7:
            raise ValueError(f"Error: Pin {pin} fuera de rango (0-7) cachon")
        # BITn → n es el número del pin
        bit_macro = f"BIT{pin}"

        lines = []
        if mode == "OUTPUT":
            lines.append(f"{name}->DIR |= {bit_macro};      // Configurar {name}.{pin} como salida")
            lines.append(f"{name}->OUT ^= {bit_macro};      // Toggle de {name}.{pin}")
        elif mode == "INPUT":
            lines.append(f"{name}->DIR &= ~{bit_macro};     // Configurar {name}.{pin} como entrada")
            lines.append(f"{name}->REN |= {bit_macro};      // Habilitar resistencia interna")
            lines.append(f"{name}->OUT |= {bit_macro};      // Configurar como pull-up")
        else:
            raise ValueError(f"Modo '{mode}' no soportado para TI.")

        return "\n".join(lines)
