# Proyecto Final - Configurador de Perifericos ARM CortexM en C

## Qué incluye
- Estructura Organizada en patrones
- Entorno virtual
- Archivo `app/main.py` con una función `greet`.
- Test con `pytest`.
- `.vscode/launch.json` para depurar en VSCode.
- `requirements.txt` y `.gitignore`.

1. **Crear y activar el entorno virtual**
   - En **PowerShell** (recomendado CMD si hay problemas con políticas):
     ```
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
     Si PowerShell bloquea la ejecución, usa CMD:
     ```
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
2. **Instalar dependencias**
   ```
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**
   - Desde el terminal:
     ```
     python -m app.main
     ```
   - O abre `app/main.py` y presiona el botón de ejecutar en VSCode.

3. **Ejecutar tests**
   ```
   pytest -q
   ```

## Notas
- `.venv` está en `.gitignore` para que no se incluya en control de versiones ni en el zip.
- (Opcional) en VSCode `Ctrl+Shift+P` -> "Python: Select Interpreter" y elige `.venv` para que la extensión use el entorno virtual.
