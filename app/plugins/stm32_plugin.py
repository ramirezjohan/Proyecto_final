
from app.plugins.registry import register_manufacturer
from app.adapters.stm32_adapter import STM32Adapter

@register_manufacturer("STM32")
class STM32Plugin:
    def get_adapter(self):
        return STM32Adapter()
