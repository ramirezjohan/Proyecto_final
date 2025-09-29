
from app.factories import PeripheralFactory
from app.strategy import CodeGenerationStrategy
from app.builders.c_code_builder import CCodeBuilder

class CodeGenerator:
    def __init__(self, manufacturer: str):
        self.strategy = CodeGenerationStrategy(manufacturer)
        self.builder = CCodeBuilder()

    def add_peripheral(self, peripheral_type, name, config):
        peripheral = PeripheralFactory.create(peripheral_type, name, config)
        code = self.strategy.generate(peripheral)
        self.builder.add_section(code)

    def build(self):
        return self.builder.build()
