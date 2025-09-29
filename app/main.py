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

import app.plugins.stm32_plugin
from app.code_generator import CodeGenerator

generator = CodeGenerator("STM32")
generator.add_peripheral("GPIO", "GPIOC", {"mode": "output", "pin": 13})

print("=== Código STM32 GPIO ===")
print(generator.build())