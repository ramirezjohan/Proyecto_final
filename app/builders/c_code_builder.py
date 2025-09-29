
from .base_builder import BaseCodeBuilder

class CCodeBuilder(BaseCodeBuilder):
    def add_gpio_init(self, port, pin):
        self.add_section(f"// Configurar GPIO {port}{pin}\n")

    def add_uart_init(self, uart, baud):
        self.add_section(f"// Configurar UART {uart} a {baud} baudios\n")
