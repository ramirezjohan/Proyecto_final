"""
from app.factories import PeripheralFactory
from app.strategy import CodeGenerationStrategy
from app.builders.c_code_builder import CCodeBuilder

class CodeGenerator:
    def __init__(self, manufacturer: str, mcu_model=None):
        self.strategy = CodeGenerationStrategy(manufacturer)
        self.builder = CCodeBuilder()

    def add_peripheral(self, peripheral_type, name, config):
        peripheral = PeripheralFactory.create(peripheral_type, name, config)
        code = self.strategy.generate(peripheral)
        self.builder.add_section(code)

    def build(self):
        return self.builder.build()"""
"""
from app.factories import PeripheralFactory
from app.strategy import CodeGenerationStrategy
from app.builders.c_code_builder import CCodeBuilder

class CodeGenerator:
    def __init__(self, manufacturer: str, mcu_model: str = None):
        self.manufacturer = manufacturer
        self.mcu_model = mcu_model       # Guardamos el modelo de micro
        self.strategy = CodeGenerationStrategy(manufacturer, mcu_model)  # Se pasa a la estrategia
        self.builder = CCodeBuilder()

    def add_peripheral(self, peripheral_type, name, config):
        peripheral = PeripheralFactory.create(peripheral_type, name, config)
        # Adjuntamos el modelo para que adapters lo lean (sin tocar la clase Peripheral)
        setattr(peripheral, "model", self.mcu_model)
        code = self.strategy.generate(peripheral)
        self.builder.add_section(code)

    def build(self):
        return self.builder.build()
        """
from app.factories import PeripheralFactory
from app.strategy import CodeGenerationStrategy
from app.builders.c_code_builder import CCodeBuilder

class CodeGenerator:
    def __init__(self, manufacturer: str, mcu_model: str = None):
        self.manufacturer = manufacturer
        self.mcu_model = mcu_model
        self.strategy = CodeGenerationStrategy(manufacturer, mcu_model)
        self.builder = CCodeBuilder()

    def add_peripheral(self, peripheral_type, name, config):
        peripheral = PeripheralFactory.create(peripheral_type, name, config)
        setattr(peripheral, "model", self.mcu_model)
        code = self.strategy.generate(peripheral)
        self.builder.add_section(code)

    def build(self):
        return self.builder.build()

