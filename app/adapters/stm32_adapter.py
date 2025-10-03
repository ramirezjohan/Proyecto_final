
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

""" from .base_adapter import BaseAdapter

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
"""
"""
from .base_adapter import BaseAdapter

class STM32Adapter(BaseAdapter):
    def generate_code(self, peripheral):
        if peripheral.peripheral_type == "GPIO":
            port = peripheral.name[-1]         # Ej: GPIOC → 'C'
            pin = peripheral.config.get("pin", 13)
            mode = peripheral.config.get("mode", "output")

            # Determinar si usar CRL o CRH
            if pin < 8:
                reg = "CRL"
                offset = pin * 4
            else:
                reg = "CRH"
                offset = (pin - 8) * 4

            code_lines = []

            # Comentario: habilitar reloj
            code_lines.append(f"// Habilitar reloj para GPIO{port}")
            if port == 'A':
                code_lines.append("RCC->APB2ENR |= (1 << 2); // IOPAEN")
            elif port == 'B':
                code_lines.append("RCC->APB2ENR |= (1 << 3); // IOPBEN")
            elif port == 'C':
                code_lines.append("RCC->APB2ENR |= (1 << 4); // IOPCEN")

            # Comentario: configuración de registro CRL/CRH
            code_lines.append(f"// Configurar GPIO{port}{pin} como salida push-pull 2MHz")
            code_lines.append(f"GPIO{port}->{reg} &= ~(0xF << {offset});")
            code_lines.append(f"GPIO{port}->{reg} |=  (0x2 << {offset}); // MODE=10, CNF=00")

            # Comentario: toggle (prueba)
            code_lines.append(f"// Toggle GPIO{port}{pin}")
            code_lines.append(f"GPIO{port}->ODR ^= (1 << {pin});")

            return "\n".join(code_lines)

        else:
            return "// Periférico no soportado aún\n"
"""

"""
from .base_adapter import BaseAdapter

class STM32Adapter(BaseAdapter):
    def generate_code(self, peripheral):
        model = getattr(peripheral, "model", "") or ""
        name = peripheral.name  # e.g. GPIOC
        port = name[-1] if name else "C"
        pin = peripheral.config.get("pin", 13)

        # --- STM32F1 family (STM32F103, etc.) -> CRL/CRH + RCC->APB2ENR
        if ("F1" in model) or ("F103" in model) or model.upper().startswith("STM32F1") or "F103" in model.upper():
            if pin < 8:
                reg = "CRL"
                offset = pin * 4
            else:
                reg = "CRH"
                offset = (pin - 8) * 4

            lines = []
            # RCC APB2ENR bits for ports A..E on F1: A=2,B=3,C=4,D=5,E=6
            port_rcc = {"A":2, "B":3, "C":4, "D":5, "E":6}
            if port in port_rcc:
                lines.append(f"RCC->APB2ENR |= (1 << {port_rcc[port]});")
            lines.append(f"GPIO{port}->{reg} &= ~(0xF << {offset});")
            lines.append(f"GPIO{port}->{reg} |=  (0x2 << {offset});")  # MODE=10 CNF=00 -> push-pull 2MHz
            lines.append(f"GPIO{port}->ODR ^= (1 << {pin});")
            return "\n".join(lines)

        # --- STM32F4/F7 family (ej. STM32F407, F767) -> MODER + RCC->AHB1ENR
        else:
            lines = []
            # RCC AHB1ENR bits example A=0,B=1,C=2,D=3,E=4 (ajusta si tu MCU usa distinto)
            port_rcc_f4 = {"A":0,"B":1,"C":2,"D":3,"E":4}
            if port in port_rcc_f4:
                lines.append(f"RCC->AHB1ENR |= (1 << {port_rcc_f4[port]});")
            lines.append(f"GPIO{port}->MODER &= ~(3 << ({pin}*2));")
            lines.append(f"GPIO{port}->MODER |=  (1 << ({pin}*2));")  # MODER=01 -> General purpose output
            lines.append(f"GPIO{port}->ODR ^= (1 << {pin});")
            return "\n".join(lines)
"""
from .base_adapter import BaseAdapter

class STM32Adapter(BaseAdapter):
    def generate_code(self, peripheral):
        model = getattr(peripheral, "model", "") or ""
        name = peripheral.name
        port = name[-1] if name else "C"
        pin = peripheral.config.get("pin", 13)

         # VALIDACIÓN DE PIN
        if not isinstance(pin, int):
            raise ValueError(f"Error: Sea serio, esta jodida es. Valor recibido: {pin}")
        if not (0 <= pin <= 15):
            raise ValueError(f"Error: Pin {pin} fuera de rango válido (0–15) para {model or 'STM32'}.")



        # STM32F1 (ej: F103) → CRL/CRH
        if ("F1" in model) or ("F103" in model) or model.upper().startswith("STM32F1"):
            if pin < 8:
                reg = "CRL"
                offset = pin * 4
            else:
                reg = "CRH"
                offset = (pin - 8) * 4

            port_rcc = {"A":2, "B":3, "C":4, "D":5, "E":6}
            lines = []
            if port in port_rcc:
                lines.append(f"RCC->APB2ENR |= (1 << {port_rcc[port]});")
            lines.append(f"GPIO{port}->{reg} &= ~(0xF << {offset});")
            lines.append(f"GPIO{port}->{reg} |=  (0x2 << {offset});")
            lines.append(f"GPIO{port}->ODR ^= (1 << {pin});")
            return "\n".join(lines)

        # STM32F4/F7 → MODER
        else:
            port_rcc_f4 = {"A":0,"B":1,"C":2,"D":3,"E":4}
            lines = []
            if port in port_rcc_f4:
                lines.append(f"RCC->AHB1ENR |= (1 << {port_rcc_f4[port]});")
            lines.append(f"GPIO{port}->MODER &= ~(3 << ({pin}*2));")
            lines.append(f"GPIO{port}->MODER |=  (1 << ({pin}*2));")
            lines.append(f"GPIO{port}->ODR ^= (1 << {pin});")
            return "\n".join(lines)
