
"""
from .base_adapter import BaseAdapter

class STM32Adapter(BaseAdapter):
    def generate_code(self, peripheral):
        if peripheral.peripheral_type == "GPIO":
            port = peripheral.name[-1]   # Ej: GPIOC → C
            pin = peripheral.config.get("pin", 0)
            return f"// STM32: Configurar GPIO {port}{pin}\n"
        elif peripheral.peripheral_type == "UART":
            baud = peripheral.config.get("baudrate", 9600)
            return f"// STM32: Configurar UART {peripheral.name} a {baud} baudios\n"
        else:
            return "// STM32: Periférico no soportado aún\n"
"""

from .base_adapter import BaseAdapter

# Plantillas básicas de configuración

GPIO_TEMPLATE = {
    "output": "GPIO{port}->MODER |= (1 << ({pin}*2));",
    "input":  "GPIO{port}->MODER &= ~(3 << ({pin}*2));"
}

UART_TEMPLATE = {
    "init": (
        "{uart}->BRR = {baud_reg};\n"
        "{uart}->CR1 |= (1 << 13); // UE: habilitar UART\n"
        "{uart}->CR1 |= (1 << 2) | (1 << 3); // RE+TE\n"
    )
}

class STM32Adapter(BaseAdapter):
    def generate_code(self, peripheral):
        if peripheral.peripheral_type == "GPIO":
            port = peripheral.name[-1]  # GPIOC -> C
            pin = peripheral.config.get("pin", 0)
            mode = peripheral.config.get("mode", "output")
            return GPIO_TEMPLATE[mode].format(port=port, pin=pin)

        elif peripheral.peripheral_type == "UART":
            uart = peripheral.name
            baud = peripheral.config.get("baudrate", 9600)
            # cálculo simple de BRR para F103 a 72MHz (ejemplo)
            baud_reg = int(72000000 / baud)
            return UART_TEMPLATE["init"].format(uart=uart, baud_reg=baud_reg)

        else:
            return "// Periférico no soportado aún\n"
