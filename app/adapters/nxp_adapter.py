
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
