# Sin Registro de plugins
"""
plugin_registry = {}

def register_manufacturer(name):
    name = name.upper() # Forzamos mayusculas
    def decorator(cls):
        plugin_registry[name] = cls
        return cls
    return decorator

def get_plugin(name):
    name = name.upper()
    if name not in plugin_registry:
        raise ValueError(f"Fabricante '{name}' no registrado")
    return plugin_registry[name]
"""

# Con registro manual de plugins

# app/plugins/registry.py
import importlib

# Diccionario manufacturer (clave mayúscula) -> clase Plugin
plugin_registry: dict = {}

def register_manufacturer(name: str):
    """Decorador (compatible con plugins existentes que usan @register_manufacturer)."""
    def decorator(cls):
        plugin_registry[name.upper()] = cls
        return cls
    return decorator

def get_plugin(name: str):
    key = name.upper()
    if key not in plugin_registry:
        raise ValueError(f"Fabricante '{name}' no registrado")
    return plugin_registry[key]

def list_registered() -> list:
    """Lista de fabricantes registrados (nombres en mayúsculas)."""
    return list(plugin_registry.keys())

def register_all_plugins(plugin_module_names: list = None):
    """
    Importa los módulos de plugin proporcionados (o una lista por defecto).
    Al importarlos, si usan @register_manufacturer se registrarán automáticamente.
    No aborta la ejecución si un plugin falla: imprime aviso y continúa.
    """
    if plugin_module_names is None:
        plugin_module_names = [
            "app.plugins.stm32_plugin",
            "app.plugins.nxp_plugin",
            "app.plugins.ti_plugin",
        ]

    for mod_name in plugin_module_names:
        try:
            importlib.import_module(mod_name)
        except Exception as e:
            # No interrumpe el proceso; solo informa para debug rápido
            print(f"No se pudo cargar plugin '{mod_name}': {e}")
