# PRMER CODIGO
"""
from .base_adapter import BaseAdapter

GPIO_TEMPLATE = {
    "output": "GPIO_PORT{port}->DIR |= (1 << {pin});",
    "input":  "GPIO_PORT{port}->DIR &= ~(1 << {pin});"
}

UART_TEMPLATE = {
    "init": (
        "{uart}->BAUD = {baud_reg};\n"
        "{uart}->CTRL |= 0x01; // enable UART\n"
    )
}

class NXPAdapter(BaseAdapter):
    def generate_code(self, peripheral):
        if peripheral.peripheral_type == "GPIO":
            port = peripheral.name[-1]
            pin = peripheral.config.get("pin", 0)
            mode = peripheral.config.get("mode", "output")
            return GPIO_TEMPLATE[mode].format(port=port, pin=pin)
        elif peripheral.peripheral_type == "UART":
            uart = peripheral.name
            baud = peripheral.config.get("baudrate", 9600)
            baud_reg = int(12000000 / baud)  # ejemplo
            return UART_TEMPLATE["init"].format(uart=uart, baud_reg=baud_reg)
        else:
            return "// Periférico no soportado aún\n"
"""
# SEGUNDO CODIGO

from .base_adapter import BaseAdapter

class NXPAdapter(BaseAdapter):
    def generate_code(self, peripheral):
        model = getattr(peripheral, "model", "") or ""
        name = peripheral.name or ""
        port = name[-1].upper() if name else "A"
        pin = peripheral.config.get("pin", 0)

        # Validación: muchos NXP/Kinetis usan puertos de 0..31
        if not isinstance(pin, int):
            raise ValueError(f"Error: El número de pin debe ser entero. Valor: {pin}")
        if not (0 <= pin <= 31):
            raise ValueError(f"Error: Pin {pin} fuera de rango válido (0–31) para {model or 'NXP'}.")

        lines = []
        # Nota: NXP tiene familias distintas (Kinetis, LPC...). Aquí usamos una generación
        # práctica y genérica (placeholders claros) que funcionan como plantilla para Keil.
        lines.append(f"/* Habilitar reloj al puerto {port} */")
        lines.append(f"SIM->SCGC5 |= ({port});\n\r")
        lines.append(f"/* Configurar MUX a GPIO */")
        lines.append(f"PORT{port}->PCR[{pin}] = PORT_PCR_MUX(1);  /* PIN como GPIO */ \n\r")

        # Dirección y toggle (PDDR/PTOR).
        lines.append(f"====PT{port} como salida==== \n\r")
        lines.append(f"PT{port}->PDDR |= (1u << {pin});\n\r")
        lines.append(f"====PT{port} en funcion del tiempo==== \n\r")
        lines.append(f"PT{port}->PTOR = (1u << {pin}); \n\r")

        return "\n".join(lines)
