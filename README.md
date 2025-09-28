# Proyecto Python para VSCode (Windows) - Ejemplo sencillo

## Qué incluye
- Estructura mínima lista para usar con VSCode en Windows.
- Entorno virtual (no incluido) instrucciones para crearlo.
- Archivo `app/main.py` con una función `greet`.
- Test con `pytest`.
- `.vscode/launch.json` para depurar en VSCode.
- `requirements.txt` y `.gitignore`.

## Pasos rápidos (Windows)

1. **Instala Python** (recomendado 3.8+): https://www.python.org/
   - Durante la instalación marca "Add Python to PATH".
   - Verifica con `python --version` en PowerShell o CMD.

2. **Instala Visual Studio Code**: https://code.visualstudio.com/
   - Abre VSCode y en Extensiones instala *Python* (Microsoft).

3. **Abrir el proyecto**
   - Extrae o coloca la carpeta `python_vs_code_project` en `C:\ruta\a\proyectos`.
   - Abre la carpeta con VSCode (File -> Open Folder).

4. **Crear y activar el entorno virtual**
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
5. **Instalar dependencias**
   ```
   pip install -r requirements.txt
   ```

6. **Ejecutar la aplicación**
   - Desde el terminal:
     ```
     python -m app.main
     ```
   - O abre `app/main.py` y presiona el botón de ejecutar en VSCode.

7. **Ejecutar tests**
   ```
   pytest -q
   ```

## Notas
- `.venv` está en `.gitignore` para que no se incluya en control de versiones ni en el zip.
- Si quieres, en VSCode presiona `Ctrl+Shift+P` -> "Python: Select Interpreter" y elige `.venv` para que la extensión use el entorno virtual.
