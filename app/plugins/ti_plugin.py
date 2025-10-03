
from app.plugins.registry import register_manufacturer
from app.adapters.ti_adapter import TIAdapter

@register_manufacturer("TI")
class TIPlugin:
    def get_adapter(self):
        return TIAdapter()
