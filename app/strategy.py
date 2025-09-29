"""
from app.adapters.stm32_adapter import STM32Adapter
# En el futuro podríamos importar más adaptadores (NXPAdapter, TIAdapter...)

class CodeGenerationStrategy:
    def __init__(self, manufacturer: str):
        self.manufacturer = manufacturer
        self.adapter = self._select_adapter()

    def _select_adapter(self):
        if self.manufacturer == "STM32":
            return STM32Adapter()
        # elif self.manufacturer == "NXP":
        #     return NXPAdapter()
        else:
            raise ValueError(f"Fabricante no soportado: {self.manufacturer}")

    def generate(self, peripheral):
        return self.adapter.generate_code(peripheral) """

from app.plugins.registry import get_plugin

class CodeGenerationStrategy:
    def __init__(self, manufacturer: str):
        self.manufacturer = manufacturer
        plugin_cls = get_plugin(manufacturer)
        self.adapter = plugin_cls().get_adapter()

    def generate(self, peripheral):
        return self.adapter.generate_code(peripheral)



