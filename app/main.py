"""Ejemplo simple: función greet y ejecutable."""
from typing import Any

def greet(name: str) -> str:
    """Devuelve un saludo simple."""
    return f"Hola {name}"

def main() -> None:
    print(greet("Mundo"))

if __name__ == "__main__":
    main()
