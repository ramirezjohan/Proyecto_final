
from app.plugins.registry import register_manufacturer
from app.adapters.nxp_adapter import NXPAdapter

@register_manufacturer("NXP")
class NXPPlugin:
    def get_adapter(self):
        return NXPAdapter()
