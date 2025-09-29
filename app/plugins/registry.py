
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
