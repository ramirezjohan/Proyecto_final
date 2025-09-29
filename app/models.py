
# Clases del dominio (MCU, Perifericos, ect.)

class MCU:
    def __init__(self, fabricante: str, modelo: str):
        self.fabricante = fabricante
        self.modelo = modelo


class Peripheral:
    def __init__(self, peripheral_type: str, name: str, config):
        self.peripheral_type = peripheral_type 
        self.name = name
        self.config = config

def __repr__(self):
    return f"<Peripheral type={self.peripheral_type}, name={self.name}, config={self.config}>"

class Config_Options:
    def __init__(self, opciones: dict):
        self.opciones = opciones
