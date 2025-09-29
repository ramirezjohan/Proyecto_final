
from app.code_generator import CodeGenerator

def run_cli():
    print("=== Generador de Código Embebido ===")

    manufacturer = input("Fabricante (ej: STM32): ").strip().upper()
    generator = CodeGenerator(manufacturer)

    while True:
        perif_type = input("Tipo de periférico (GPIO/UART) o 'fin' para terminar: ").strip()
        if perif_type.lower() == "fin":
            break

        name = input("Nombre del periférico (ej: GPIOC, USART3): ").strip()
        config = {}

        if perif_type.upper() == "GPIO":
            pin = int(input("Número de pin: "))
            mode = input("Modo (input/output): ").strip()
            config = {"pin": pin, "mode": mode}

        elif perif_type.upper() == "UART":
            baud = int(input("Baudrate: "))
            config = {"baudrate": baud}

        generator.add_peripheral(perif_type.upper(), name, config)

    print("\n=== Código Generado ===")
    print(generator.build())
