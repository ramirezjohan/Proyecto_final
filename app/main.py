"""Ejemplo simple: función greet y ejecutable."""
import app.models
import app.services
import app.utils

"""
# Prueba de funcionamiento paso 4

from app.models import MCU, Peripheral, Config_Options

mcu = MCU("STM32", "F103C8")
gpio = Peripheral("GPIO", "GPIOA", {"mode": "output", "pin": 5})
opts = Config_Options({"mode": "output", "pin": 5})

print("Dominio OK:", mcu.fabricante, gpio.name, opts.opciones)

# Prueba de funcionamiento paso 5

from app.models import MCU, Peripheral
from app.generators.c_generator import CGenerator

mcu = MCU("ST", "F767ZI")
peripherals = [Peripheral("GPIO", "GPIOC", {"mode": "output", "pin": 13}), 
               Peripheral("USART", "UART3", {"baudrate": 115200})]

gen = CGenerator()
print(gen.generate(mcu, peripherals))

# Prueba de funcionamiento paso 6

from app.builders.c_code_builder import CCodeBuilder

builder = CCodeBuilder()
builder.add_gpio_init("C", 13)
builder.add_uart_init("USART3", 115200)

codigo_final = builder.build()
print(codigo_final)

# Prueba de funcionamiento paso 7 - Factory patern
from app.factories import PeripheralFactory

gpio = PeripheralFactory.create("GPIO", "GPIOB", {"mode": "input", "pin": 2})
uart = PeripheralFactory.create("UART", "USART1", {"baudrate": 9600})

print("Factory GPIO:", gpio.name, gpio.config)
print("Factory UART:", uart.name, uart.config)


## Prueba de funcionamiento paso 8

from app.factories import PeripheralFactory
from app.adapters.stm32_adapter import STM32Adapter

# Crear periféricos genéricos
gpio = PeripheralFactory.create("GPIO", "GPIOC", {"mode": "output", "pin": 13})
uart = PeripheralFactory.create("UART", "USART3", {"baudrate": 115200})

# Usar adaptador STM32
adapter = STM32Adapter()
print(adapter.generate_code(gpio))
print(adapter.generate_code(uart))


## Prueba de funcionamiento paso 9

from app.factories import PeripheralFactory
from app.strategy import CodeGenerationStrategy

# Periféricos genéricos
gpio = PeripheralFactory.create("GPIO", "GPIOC", {"mode": "output", "pin": 13})
uart = PeripheralFactory.create("UART", "USART3", {"baudrate": 115200})

# Seleccionar fabricante
strategy = CodeGenerationStrategy("STM32")

# Generar código para cada periférico
print(strategy.generate(gpio))
print(strategy.generate(uart))

## Prueba de funcionamiento paso 10

from app.code_generator import CodeGenerator

generator = CodeGenerator("STM32")
generator.add_peripheral("GPIO", "GPIOC", {"mode": "output", "pin": 13})
generator.add_peripheral("UART", "USART3", {"baudrate": 115200})

final_code = generator.build()
print("=== Código Final ===")
print(final_code)
"""
# Prueba de paso 11 - Plugins
"""
import app.plugins.stm32_plugin
from app.code_generator import CodeGenerator

# Ya STM32 está registrado como plugin automáticamente
generator = CodeGenerator("STM32")
generator.add_peripheral("GPIO", "GPIOC", {"mode": "output", "pin": 13})
generator.add_peripheral("UART", "USART3", {"baudrate": 115200})

final_code = generator.build()
print("=== Código Final con Plugin ===")
print(final_code)
"""

#from app.cli import run_cli

#if __name__ == "__main__":
 #   run_cli()

"""from app.code_generator import CodeGenerator

generator = CodeGenerator("STM32")
generator.add_peripheral("GPIO", "GPIOC", {"mode": "output", "pin": 13})
generator.add_peripheral("UART", "USART3", {"baudrate": 115200})

print("=== Código Real STM32 ===")
print(generator.build())
"""


"""from app.code_generator import CodeGenerator

generator = CodeGenerator("STM32")
generator.add_peripheral("GPIO", "GPIOC", {"mode": "output", "pin": 8})

print("=== Código STM32 GPIO ===")
print(generator.build())"""
from app.code_generator import CodeGenerator

"""
def main():
    print("=== Generador de Código para Keil UV5 ===")

    # Pedir fabricante y modelo
    manufacturer = input("Fabricante (ej: STM32): ").strip()
    mcu_model = input("MCU_model: ").strip()

    try:
        generator = CodeGenerator(manufacturer, mcu_model)
    except ValueError as e:
        print(f"La cagaste Mk: {e}")
        return
    
    # Validar perifericos para continuar
    valid_peripherals = ["GPIO", "USART", "TIM", "ADC"]
    peripheral_type = input("Tipo de periférico (ej: GPIO): ").strip().upper()

    # Crear instancia del generador
    generator = CodeGenerator(manufacturer, mcu_model)

    # Pedir periférico
    peripheral_type = input("Tipo de periférico (ej: GPIO): ").strip()
    name = input("Nombre (ej: GPIOC): ").strip()

    # Configuración básica para gpio
    config = {}
    if peripheral_type.upper() == "GPIO":
        mode = input("Modo (output/input): ").strip()
        pin = int(input("Número de pin (ej: 13): ").strip())
        config = {"mode": mode, "pin": pin}

    # Añadir periférico y generar código
    generator.add_peripheral(peripheral_type, name, config)

    print("\n=== Código generado ===")
    print(generator.build())

if __name__ == "__main__":
    main()
"""
# -------------------------------------------------------
"""
from app.code_generator import CodeGenerator

def main():
    print("=== Generador de Código para Keil UV5 ===")

    # Pedir fabricante y modelo
    manufacturer = input("Fabricante (ej: STM32): ").strip()
    mcu_model = input("MCU_model: ").strip()

    try:
        generator = CodeGenerator(manufacturer, mcu_model)
    except ValueError as e:
        print(f"La cagaste Mk: {e}")
        return

    # Validar periférico antes de continuar
    valid_peripherals = ["GPIO", "USART", "TIM", "ADC"]
    peripheral_type = input("Tipo de periférico (ej: GPIO): ").strip().upper()

    if peripheral_type not in valid_peripherals:
        print(f"Esta verga'{peripheral_type}' no es un periférico válido.")
        return

    name = input("Nombre (ej: GPIOC): ").strip()

    # Configuración básica para GPIO
    config = {}
    if peripheral_type == "GPIO":
        mode = input("Modo (output/input): ").strip()
        pin = int(input("Número de pin (ej: 13): ").strip())
        config = {"mode": mode, "pin": pin}

    generator.add_peripheral(peripheral_type, name, config)

    print("\n=== Código generado ===")
    print(generator.build())


if __name__ == "__main__":
    main()
"""
## Nuevo codigo con validacion de entradas
"""
from app.code_generator import CodeGenerator

def main():
    print("=== Generador de Código para Keil UV5 ===")

    # Paso 1 — Leer y normalizar entradas
    manufacturer = input("Fabricante (ej: STM32): ").strip().upper()
    mcu_model = input("MCU_model: ").strip().upper()
    peripheral_type = input("Tipo de periférico (ej: GPIO): ").strip().upper()
    name = input("Nombre (ej: GPIOC): ").strip().upper()

    # Paso 2 — Validar entradas básicas
    VALID_MANUFACTURERS = ["STM32"]
    VALID_MCUS = ["STM32F103", "STM32F407"]
    VALID_PERIPHERALS = ["GPIO"]

    if manufacturer not in VALID_MANUFACTURERS:
        print(f"Error: '{manufacturer}' no es un fabricante válido.")
        return

    if mcu_model not in VALID_MCUS:
        print(f"Error: '{mcu_model}' no es un modelo MCU válido.")
        return

    if peripheral_type not in VALID_PERIPHERALS:
        print(f"Error: '{peripheral_type}' no es un periférico válido.")
        return

    # 🪜 Paso 3 — Configuración específica del periférico GPIO
    config = {}
    if peripheral_type == "GPIO":
        mode = input("Modo (OUTPUT/INPUT): ").strip().upper()
        if mode not in ["OUTPUT", "INPUT"]:
            print(f"Error: '{mode}' no es un modo válido.")
            return
        config["mode"] = mode

        try:
            pin_number = int(input("Número de pin (ej: 13): ").strip())
            config["pin"] = pin_number
        except ValueError:
            print("Error: el número de pin debe ser un entero.")
            return

    # Paso 4 — Generar código
    generator = CodeGenerator(manufacturer, mcu_model)
    generator.add_peripheral(peripheral_type, name, config)
    final_code = generator.build()

    print("\n=== Código generado ===")
    print(final_code)

if __name__ == "__main__":
    main()
"""

import app.plugins.stm32_plugin
import app.plugins.nxp_plugin
import app.plugins.ti_plugin

from app.code_generator import CodeGenerator

def main():
    print("=== Generador de Código para Keil UV5 ===")

    # Paso 1 — Leer y normalizar entradas
    manufacturer = input("Fabricante (ej: STM32): ").strip().upper()
    mcu_model = input("MCU_model: ").strip().upper()
    peripheral_type = input("Tipo de periférico (ej: GPIO): ").strip().upper()
    name = input("Nombre (ej: GPIOC): ").strip().upper()

    # Paso 2 — Validar entradas básicas
    VALID_MANUFACTURERS = ["STM32", "NXP", "TI"]
    VALID_MCUS = ["STM32F103", "STM32F407", "MKL25Z4", "MK20D50M", "MSP432P401R"]
    VALID_PERIPHERALS = ["GPIO", "UART"]

    if manufacturer not in VALID_MANUFACTURERS:
        print(f"Error: '{manufacturer}' no es un fabricante válido.")
        return

    if mcu_model not in VALID_MCUS:
        print(f"Error: '{mcu_model}' no es un modelo MCU válido.")
        return

    if peripheral_type not in VALID_PERIPHERALS:
        print(f"Error: '{peripheral_type}' no es un periférico válido.")
        return

    # Paso 3 — Configuración específica del periférico GPIO
    config = {}
    if peripheral_type == "GPIO":
        mode = input("Modo (OUTPUT/INPUT): ").strip().upper()
        if mode not in ["OUTPUT", "INPUT"]:
            print(f"Error: '{mode}' no es un modo válido.")
            return
        config["mode"] = mode

        try:
            pin_number = int(input("Número de pin (ej: 13): ").strip())
            config["pin"] = pin_number
        except ValueError:
            print("Error: el número de pin debe ser un entero.")
            return

    # Paso 4 — Generar código con control de errores
    try:
        generator = CodeGenerator(manufacturer, mcu_model)
        generator.add_peripheral(peripheral_type, name, config)
        final_code = generator.build()

        print("\n=== Código generado ===")
        print(final_code)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
